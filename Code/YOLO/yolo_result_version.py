from ultralytics import YOLO
import cv2
import numpy as np
import time
from tqdm import tqdm # for progress bar
from DCE.DCE import *




def get_outline_for_every_object(res, options): 
    """
    Draws the outlines for each object that YOLO has detected

    @param: res: result object from yolo; array
    @param options: Dictionary with options set in main
    """
    fps = len(res)  #number of all frames
    res_cop = res
    NoP = get_number_of_points_result(res)  #get total number of points for all objects in the result file (the video)
    pbar = tqdm(desc= "DCE Progress", total = NoP) #init progress bar

    for i in range(fps): #iterate over all video frames
        if (res[i] is not None):    #if clause if yolo detected no object at the frame
            data_arr = get_data(res[i]) #returns the data, that YOLO detectet at the frame [0] = bbox, [1] = class ids, [2] = segmentation contours; [3] = scores for every object, [4] = image size
    
            bbox = data_arr[0]
            class_id = data_arr[1]
            scores = data_arr[3]
            img_size = data_arr[4]

            options["timestamp_DCE_start"] = time.time()
            outline_DCE = run_DCE(data_arr[2],data_arr[1] ,options) #run DCE with polygons that yolo detected in the frame, the class_ids for every object; the actual number of points and the options dataset

            if(options["save_timestamps"]==True):
                options["timestamp_DCE_end"] = time.time()
                options["timestamp_DCE_dur"] = options["timestamp_DCE_dur"] + (options["timestamp_DCE_end"] - options["timestamp_DCE_start"])

            res_cop[i]= cv2.polylines(res[i].orig_img, outline_DCE, True, (255, 255, 255), 0) #draw the with DCE simplified polygons

            if(options["black_video"] == True): #If clause to set the result video to black
                res_cop[i] = cv2.rectangle(res_cop[i], (0,0),(img_size[0],img_size[1]), (0, 0, 0), -1)
          
            for b in range(len(bbox)): #iterate over every polygon to write a individual label for all polygons on the frame
               
                res_cop[i] = cv2.rectangle(res_cop[i], (bbox[b][0],bbox[b][1]),(bbox[b][2],bbox[b][3]), (0, 0, 0), -1)

                if(options["write_labels"] == True): #if clause to write the labels and scores to every polygon
                    res_cop[i] = cv2.putText(res_cop[i], get_text_string(class_id[b],scores[b]), (bbox[b][0], bbox[b][1] - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                pbar.update(1) #set progress bar one step further
    
                sum_of_angles = get_sum_of_angles([outline_DCE[b]]) #calculates the sum of angles in one polygon
                options["angle_sums_polygons"].append(sum_of_angles)  #append sum of angles in one polygon to a array, where all angle sums of the polygons in the image saved    

                options["list_of_polygons_in_one_frame"].append([i,b,sum_of_angles,class_id[b],outline_DCE[b]])
                
            options["angle_sums_images"].append(sum(options["angle_sums_polygons"])) #sum up all angle sums in the image and append it to an array, where all sum of angles from all images would be saved
            options["angle_sums_polygons"] = [] # set for the next image the variable, which saved the sum of all angles from all polygon in the image,  to None/0
          
            options["list_of_all_polygons"].append(options["list_of_polygons_in_one_frame"])
            options["list_of_polygons_in_one_frame"] = []
            options["number_of_polygons"] = options["number_of_polygons"] + len(bbox)

            res_cop[i]= cv2.polylines(res[i], outline_DCE, True, (255, 255, 255), 1)  #draw simplified polygon on the specific frame

        else: # if there is no object detected. the whole frame must be set black
            res_cop[i]= cv2.polylines(res[i].orig_img, outline_DCE, True, (255, 255, 255), 0) 
            pbar.update(1) #set progress bar one step further
            if(options["black_video"] == True):
                res_cop[i] = cv2.rectangle(res_cop[i], (0,0),(img_size[0],img_size[1]), (0, 0, 0), -1)
                
    pbar.close() #close progress bar
    return [res_cop, options] #return result object with simplified polygons and options file with




def run_DCE(outline, class_id, options): 
    """
    Calculate DCE on an input array for the given object with given scores.

    @param outline = 2-dim array; all from YOLO detected polygons on a given frame
    @param class_ID = array, which the class_IDs from all detected objects on the image saved; only ints
    @param options: Dictionary with options set in main
    @return: array with simplified olygons
    """         
    for i in range(len(outline)): #iterate over all polygons in the outline array
        match class_id[i]: #case case to distinguish the different CLass IDs; 2 = Car, 3 = motorcycle, 7 = Truck
            case 2:
                outline[i] = simplify_polygon_k_with_angle(outline[i],options["NoP_Cars"], options)
            case 3:
                outline[i] = simplify_polygon_k_with_angle(outline[i],options["NoP_Motorcycle"], options)
            case 7:
                outline[i] = simplify_polygon_k_with_angle(outline[i],options["NoP_Truck"], options)
            case _:
                outline[i] = simplify_polygon_k_with_angle(outline[i],options["NoP_other_Object"], options) 
    return outline




def get_data(res):
    """
    returns data from a result file element, which was created by YOLO

    @param res: one element in result file array
    @return: bboxes, class_ids, segmentation_contours_idx, scores, img_size as array
    """
    segmentation_contours_idx = []
    height, width, layers = res.orig_img.shape
    img_size = [width, height]
    bboxes = np.array([])
    class_ids = np.array([])
    scores = np.array([])
    if res.masks is not None:
        segmentation_contours_idx = res.masks.xy
        bboxes = np.array(res.boxes.xyxy.cpu(), dtype="int") #cast as int, to get integers
        # Get class ids
        class_ids = np.array(res.boxes.cls.cpu(), dtype="int") #cast as int, to get integers
        # Get scores
        scores = np.array(res.boxes.conf.cpu(), dtype="float").round(2)
    return bboxes, class_ids, segmentation_contours_idx, scores, img_size




def get_number_of_points_result(res):
    """
    returns total number of points in a result object

    @param res: Object which was created by Yolo and contains all detected objects and frames
    @return: NoP; Number of Points as int
    """
    NoP = 0
    for i in range(len(res)):
        NoP = NoP + len(res[i])
    return NoP




def get_text_string(class_id, score):
    """
    return a text string from a given class id with the individual score for every polygon 

    @param class_id = int to identify the class
    @return: string
    """
    category_list = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}
    category = category_list[class_id]
    return (category + str(score))




def write_video(res, path_write_video, path_source_video):
    """
    create a video from a given result object, which was created by YOLO

    @param res = result array, which was createt by YOLO and contains all frames with polygons
    @param path_source_video = File path where the source video is located
    @param path_write_video = File path where the result video will be stored
    @return: 0

    Source: https://stackoverflow.com/questions/43048725/python-creating-video-from-images-using-opencv
    """
    height, width, layers = res[2].shape
    fps = int(get_fps(path_source_video))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    video=cv2.VideoWriter(path_write_video,fourcc,fps,(width,height))
    for i in range(len(res)):
        video.write(res[i])
    cv2.destroyAllWindows()
    video.release()
    print("video saved")
    return 0




def get_fps(path):  
    """
    return the frames per second (fps)

    @param path: path to identifiy the video
    @return: length a int

    Source: https://stackoverflow.com/questions/49025795/python-opencv-video-getcv2-cap-prop-fps-returns-0-0-fps
    """
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    return fps