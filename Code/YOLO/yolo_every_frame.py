from ultralytics import YOLO # ?? codesource: https://towardsdatascience.com/enhanced-object-detection-how-to-effectively-implement-yolov8-afd1bf6132ae ????
import pandas # Source: https://java2blog.com/save-object-to-file-python/
import numpy as np
import cv2
import time
from tqdm import tqdm # for progress bar
from YOLO.yolo_segmentation import YOLOSegmentation
from DCE.DCE import *




def run_yolo_every_frame_version_intern(options):
    """
    run yolo for every frame

    The source video is split into individual frames. Yolo is then applied to each individual frame. After that, the detected outlines are simplified with DCE and placed in the image. As a final step, the individual frames are reassembled into a video.

    @param options: Dictionary with options set in main
    """

    framecounter = get_number_of_frames(options["path_source_video"]) #get total number of frames from source video
    pbar = tqdm(desc= "DCE Progress", total = framecounter) #init the progress bar
    img_arr=[] #image array (would be reassemblet into the video at the end)
  
    for i in range(framecounter): #iterate over all frames
        img = get_specific_frame(options["path_source_video"],i) #get specific frame from source video

        img_analyzed = run_yolo(img, options,i) #run yolo on specific frame
        
        img_arr.append(img_analyzed) #add analyzied image to array
        pbar.update(1) #set progress bar one step further
        #cv2.imwrite(r'Code\YOLO\frames\analyzed\frame'+str(i)+'.png', img_analyzed)  # save frame as JPEG file
    pbar.close()

    options["timestamp_write_video_start"] = time.time()
    create_video_from_imgs(options["path_source_video"], options["path_write_video"],img_arr, framecounter) # write video to given path
    if(options["save_timestamps"]==True):
                options["timestamp_write_video_end"] = time.time()
                options["timestamp_write_video_dur"] = options["timestamp_write_video_dur"] + (options["timestamp_write_video_end"] - options["timestamp_write_video_start"])

    return 0   
  



def run_yolo(img, options,framenumber):  
    """
    run YOLO algorithm on a given image

    @param img: single image (extracted by CV2)
    @param options: Dictionary with options set in main
    @return: img: image which was analyzed with yolo and where the polygons are drawn

    Source: https://pysource.com/2023/02/21/yolo-v8-segmentation
    """

    options["timestamp_yolo_start"] = time.time() 
    ys = YOLOSegmentation("yolov8n-seg.pt") #Selection of Yolo Algorithm
    if(options["save_timestamps"]==True):
                options["timestamp_yolo_end"] = time.time()
                options["timestamp_yolo_dur"] = options["timestamp_yolo_dur"] + (options["timestamp_yolo_end"] - options["timestamp_yolo_start"])

    bboxes, classes, segmentations, scores = ys.detect(img) #Saving the results provided by YOLO
   
    if(options["black_video"] == True): #If clause to set the result video to black
        img_size = get_img_size(img)
        img = cv2.rectangle(img, (0,0),(img_size[0],img_size[1]), (0, 0, 0), -1)

    iterator = 0
    for bbox, class_id, seg, score in zip(bboxes, classes, segmentations, scores): #Iterate over all YOLO results for drawing the polygons
       
        (x, y, x2, y2) = bbox
        options["timestamp_DCE_start"] = time.time()

        outline = run_DCE([seg], class_id, options) #run DCE for detected polygons

        if(options["save_timestamps"]==True):
                options["timestamp_DCE_end"] = time.time()
                options["timestamp_DCE_dur"] = options["timestamp_DCE_dur"] + (options["timestamp_DCE_end"] - options["timestamp_DCE_start"])
        options["timestamp_write_outline_start"] = time.time()

        cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), 2)
        cv2.polylines(img, outline, True, (255, 255, 255), 1)
      
        if(options["write_labels"] == True): #if clause to write the labels and scores to every polygon
            img = cv2.putText(img, get_text_string(class_id,score), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        #cv2.putText(img, str(class_id), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        if(options["save_timestamps"]==True):
                options["timestamp_write_outline_end"] = time.time()
                options["timestamp_write_outline_dur"] = options["timestamp_write_outline_dur"] + (options["timestamp_write_outline_end"] - options["timestamp_write_outline_start"])
    
        sum_of_angles = get_sum_of_angles(outline) #calculates the sum of angles in one polygon)
        options["angle_sums_polygons"].append(sum_of_angles) #append sum of angles in one polygon to a array, where all angle sums of the polygons in the image saved 
        
        options["list_of_polygons_in_one_frame"].append([framenumber,iterator,sum_of_angles,class_id,outline])
        iterator+=1
    
    options["list_of_all_polygons"].append(options["list_of_polygons_in_one_frame"])
    options["list_of_polygons_in_one_frame"] = []

    options["number_of_polygons"] = options["number_of_polygons"] + iterator



    options["angle_sums_images"].append(sum(options["angle_sums_polygons"])) #sum up all angle sums in the image and append it to an array, where all sum of angles from all images would be saved
    options["angle_sums_polygons"] = [] # set for the next image the variable, which saved the sum of all angles from all polygon in the image,  to None/0

    return img
        


    
def run_DCE(yolo_res_img, class_id, options):
    """
    Calculate DCE on an input array for the given object with given scores.

    @param yolo_res_img = array; all from YOLO detected polygons on a given image
    @param class_ID = array, which the class_IDs from all detected objects on the image saved; only ints
    @param img_arr = array, which contains the individual images (frames)
    @param options: Dictionary with options set in main
    @return: image with simplified polygons
    """
    
    cop_yolo_res_img = np.array(yolo_res_img, dtype=  'int')
    cop_yolo_res_img = cop_yolo_res_img[0]
 

    match class_id:  #case case to distinguish the different CLass IDs; 2 = Car, 3 = motorcycle, 7 = Truck
        case 2:
            cop_yolo_res_img = simplify_polygon_k_with_angle(cop_yolo_res_img,options["NoP_Cars"], options)
        case 3:
            cop_yolo_res_img = simplify_polygon_k_with_angle(cop_yolo_res_img,options["NoP_Motorcycle"], options)
        case 7:
            cop_yolo_res_img = simplify_polygon_k_with_angle(cop_yolo_res_img,options["NoP_Truck"], options)
        case _:
            cop_yolo_res_img = simplify_polygon_k_with_angle(cop_yolo_res_img,options["NoP_other_Object"], options)
             
    return [cop_yolo_res_img]
        
   


def create_video_from_imgs(path_source_video,path_write_video, img_arr, framecounter): 
    """
    create a video from a given array, which is filled with images

    @param path_source_video = File path where the source video is located
    @param path_write_video = File path where the result video will be stored
    @param img_arr = array, which contains the individual images (frames)
    @param framecounter = int, which represent the total number of frames from source video
    @return: 0

    Source: https://stackoverflow.com/questions/43048725/python-creating-video-from-images-using-opencv
    """
    height, width, layers = get_specific_frame(path_source_video, (framecounter)).shape
    fps = get_fps(path_source_video)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    video=cv2.VideoWriter(path_write_video,fourcc,fps,(width,height)) # cv2 write object ()
    for i in range(framecounter): #iterate to write every frame to the result video
        video.write(img_arr[i])
    cv2.destroyAllWindows()
    video.release()
    print("video saved")
    return 0
    
 
    


def get_text_string(class_id, score):
    """
    return a text string from a given class id with the individual score for every polygon 

    @param class_id = int to identify the class
    @return: string
    """
    category_list = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}
    category = category_list[class_id]
    return (category + str(score))   




def get_img_size(img):
    """
    return the width and the heigh of a given image in pixel

    @param class_id = int to identify the class
    @return: array
    """
    height, width, layers = img.shape
    img_size = [width, height]
    return img_size



def get_number_of_frames(path):  
    """
    return number of all frames in video

    @param path: path to identifiy the video
    @return: nt

    Source: https://stackoverflow.com/questions/49025795/python-opencv-video-getcv2-cap-prop-fps-returns-0-0-fps
    """
    cap = cv2.VideoCapture(path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length



def get_fps(path):
    """
    return the frames per second (fps)

    @param path: path to identifiy the video
    @return fps: int 

    Source: #https://stackoverflow.com/questions/49025795/python-opencv-video-getcv2-cap-prop-fps-returns-0-0-fps
    """
      
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    return fps




def get_specific_frame(path, frame_number): 
    """
    return a specific frame from the source path

    @param path: path to identifiy the video
    @param framenumber: number, which frame must be returned
    @return: frame as int

    Source: https://stackoverflow.com/questions/33650974/opencv-python-read-specific-frame-using-videocapture
    """
    if frame_number == 0:
        frame_number = 1
    cap = cv2.VideoCapture(path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number-1)
    res, frame = cap.read()

    #frame_resized = cv2.resize(frame, None, fx=1, fy=1) #resize frame for showing on windows
    #cv2.imwrite(r'Code\YOLO\frames\raw\frame'+str(frame_number)+'.png', frame)  # save frame as JPEG file

    return frame   