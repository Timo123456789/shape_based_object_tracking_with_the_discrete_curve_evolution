from ultralytics import YOLO
import cv2
import numpy as np
from DCE.DCE import *



def test():
    path_source_video = r'Code\vid_examples\right_Side\autobahn_2.mp4'
    path_write_video = r'Code\YOLO\runs\videos_from_frames\video_results.mp4'


    model = YOLO('yolov8n-seg.pt') 
    results = model.predict(path_source_video, save=False)
   
    print(results[3].masks.xy)
    print(len(results))

 
    res_outline = get_outline_for_every_object(results)

    write_video(res_outline, path_write_video, path_source_video)
   
  

def get_outline_for_every_object(res, options): #, NoP_Motorcycle, NoP_Truck, NoP_other_Object,black_video
    fps = len(res)
    res_cop = res
    NoP = get_number_of_points_result(res)


    for i in range(fps):
        if (res[i] is not None):
            print("Segment gefudnen")
            data_arr = get_data(res[i])
            #write_results_file(data_arr, 'data_arr')
            bbox = data_arr[0]
            class_id = data_arr[1]
            outline = data_arr[2]
            outline_DCE = run_DCE(data_arr[2],data_arr[1],options) #Hier kann DCE gut angewendet werden?
            scores = data_arr[3]
            img_size = data_arr[4]

        
            res_cop[i]= cv2.polylines(res[i].orig_img, outline_DCE, True, (255, 255, 255), 0) 
            if(options["black_video"] == True):
                res_cop[i] = cv2.rectangle(res_cop[i], (0,0),(img_size[0],img_size[1]), (0, 0, 0), -1)


            for b in range(len(bbox)):
                NoP = NoP-1
                #res_cop[i]= cv2.polylines(res[i].orig_img, outline[b], True, (0, 0, 255), 1) 
                res_cop[i] = cv2.rectangle(res_cop[i], (bbox[b][0],bbox[b][1]),(bbox[b][2],bbox[b][3]), (0, 0, 0), -1)
                if(options["write_labels"] == True):
                    res_cop[i] = cv2.putText(res_cop[i], get_text_string(class_id[b],scores[b]), (bbox[b][0], bbox[b][1] - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            res_cop[i]= cv2.polylines(res[i], outline_DCE, True, (255, 255, 255), 1) 
            print('NoP', NoP)
        else:
            print("Segment NIHCTgefudnen")
            res_cop[i]= cv2.polylines(res[i].orig_img, outline_DCE, True, (255, 255, 255), 0) 
            if(options["black_video"] == True):
                res_cop[i] = cv2.rectangle(res_cop[i], (0,0),(img_size[0],img_size[1]), (0, 0, 0), -1)
    return res_cop

def get_number_of_points_result(res):
    NoP = 0
    for i in range(len(res)):
        NoP = NoP + len(res[i])
    return NoP

def write_results_file(results, text):
    f = open( r'Code\YOLO\temp\t_'+ text+'.txt', 'w' )
    f.write(repr(results))
    f.close()
    


def run_DCE(outline, class_id, options): #car = 2,  motorcycle = 3, truck = 7,
   
    match options["calc_K_with_Dist"]:
        case True:
            for i in range(len(outline)):
                match class_id[i]:
                    case 2:
                        outline[i] = simplify_polygon_k_with_dist(outline[i],options["NoP_Cars"])
                    case 3:
                        outline[i] = simplify_polygon_k_with_dist(outline[i],options["NoP_Motorcycle"])
                    case 7:
                        outline[i] = simplify_polygon_k_with_dist(outline[i],options["NoP_Truck"])
                    case _:
                        outline[i] = simplify_polygon_k_with_dist(outline[i],options["NoP_other_Object"])

        case False:
            for i in range(len(outline)):
                match class_id[i]:
                    case 2:
                        outline[i] = simplify_polygon_k_with_angle(outline[i],options["NoP_Cars"])
                    case 3:
                        outline[i] = simplify_polygon_k_with_angle(outline[i],options["NoP_Motorcycle"])
                    case 7:
                        outline[i] = simplify_polygon_k_with_angle(outline[i],options["NoP_Truck"])
                    case _:
                        outline[i] = simplify_polygon_k_with_angle(outline[i],options["NoP_other_Object"])
        case _:
            print("Error at 'calc_K_with_Dist' Options parameter; must be True or False!")
            return None        
       
    return outline












def get_text_string(class_id, score):
    category_list = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}
    category = category_list[class_id]
    return (category + str(score))


def get_data(res):
    segmentation_contours_idx = []
    height, width, layers = res.orig_img.shape
    img_size = [width, height]
    bboxes = np.array([])
    class_ids = np.array([])
    scores = np.array([])
    if res.masks is not None:
    
        
        segmentation_contours_idx = res.masks.xy
        bboxes = np.array(res.boxes.xyxy.cpu(), dtype="int")
        # Get class ids
        class_ids = np.array(res.boxes.cls.cpu(), dtype="int")
        # Get scores
        scores = np.array(res.boxes.conf.cpu(), dtype="float").round(2)
    
    return bboxes, class_ids, segmentation_contours_idx, scores, img_size


def write_outline(img,arr):
    #print(len(arr), arr.size)

    for i in range(len(arr)):
        img[arr[i][0],arr[i][1]]=(255,0,0)
    testimg = img
    cv2.imshow("result", testimg)       
    cv2.waitKey(0)
    return img





# bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
#         # Get class ids
#         class_ids = np.array(result.boxes.cls.cpu(), dtype="int")
#         # Get scores
#         scores = np.array(result.boxes.conf.cpu(), dtype="float").round(2)




def write_video(res, path_write_video, path_source_video):
    height, width, layers = res[2].shape
    fps = int(get_fps(path_source_video))
    print(fps)
    video=cv2.VideoWriter(path_write_video,-1,fps,(width,height))
    for i in range(len(res)):
        video.write(res[i])
    cv2.destroyAllWindows()
    video.release()
    print("video saved")
    return 0


def get_number_of_frames(path): #https://stackoverflow.com/questions/25359288/how-to-know-total-number-of-frame-in-a-file-with-cv2-in-python
    cap = cv2.VideoCapture(path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(length)
    return length

def get_fps(path):  #https://stackoverflow.com/questions/49025795/python-opencv-video-getcv2-cap-prop-fps-returns-0-0-fps
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    return fps


#test()


