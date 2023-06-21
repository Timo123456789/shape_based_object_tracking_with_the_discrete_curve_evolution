#codesource: https://towardsdatascience.com/enhanced-object-detection-how-to-effectively-implement-yolov8-afd1bf6132ae

from ultralytics import YOLO
import pandas # Source: https://java2blog.com/save-object-to-file-python/
import numpy as np
import cv2
import time
from YOLO.yolo_segmentation import YOLOSegmentation
from DCE.DCE import *



#masks2segment example : https://stackoverflow.com/questions/75545012/yolov8-segmentation-mask-problem-masks-looks-2-parts-but-outputs-only-first-par



def test(): 
    #path_source_video = r'Code\vid_examples\right_Side\autobahn_2.mp4'
    path_source_video = r'Code\vid_examples\right_Side\autobahn1s.mp4'
    path_read_imgs = r'Code\YOLO\frames\analyzed\frame'
    path_write_video = r'Code\YOLO\runs\videos_from_frames\videotest_9.mp4'
    # 8n = sehr schnell, aber ungenau, 8m = schnell recht genau, 8x = langsam aber sehr genau
    #results = analyse_vid(path)

    framecounter = get_number_of_frames(path_source_video)
    fps = get_fps(path_read_imgs)
    print("framecounter")
    print(framecounter)
    img_arr=[]
    for i in range(framecounter):
        img = get_specific_frame(path_source_video,i)
      
        img_analyzed = run_yolo(img)
        
        img_arr.append(img_analyzed)
        #cv2.imwrite(r'Code\YOLO\frames\analyzed\frame'+str(i)+'.png', img_analyzed)  # save frame as JPEG file


          

 
    create_video_from_imgs(path_source_video,path_write_video,img_arr, framecounter)



def run_yolo_every_frame_version_intern(options):
    framecounter = get_number_of_frames(options["path_source_video"])
    # print("framecounter")
    # print(framecounter)
    img_arr=[]
    for i in range(framecounter):
        img = get_specific_frame(options["path_source_video"],i)

      
        img_analyzed = run_yolo(img, options)
        

        img_arr.append(img_analyzed)
        #cv2.imwrite(r'Code\YOLO\frames\analyzed\frame'+str(i)+'.png', img_analyzed)  # save frame as JPEG file


          

    options["timestamp_write_video_start"] = time.time()
    create_video_from_imgs(options["path_source_video"],options["path_write_video"],img_arr, framecounter)
    if(options["save_timestamps"]==True):
                options["timestamp_write_video_end"] = time.time()
                options["timestamp_write_video_dur"] = options["timestamp_write_video_dur"] + (options["timestamp_write_video_end"] - options["timestamp_write_video_start"])

    return 0   
  


def create_video_from_imgs(path_source_video,path_write_video, img_arr, framecounter): #https://stackoverflow.com/questions/43048725/python-creating-video-from-images-using-opencv
    height, width, layers = get_specific_frame(path_source_video, (framecounter)).shape
    fps = get_fps(path_source_video)
    video=cv2.VideoWriter(path_write_video,-1,fps,(width,height))
    for i in range(framecounter):
        video.write(img_arr[i])
    cv2.destroyAllWindows()
    video.release()
    print("video saved")
    return 0
    
 
    

 
        

  
    
def run_DCE(yolo_res_img, class_id, options):
    
    
    cop_yolo_res_img = np.array(yolo_res_img, dtype=  'int')
    cop_yolo_res_img = cop_yolo_res_img[0]
 
    match options["calc_K_with_Dist"]:
            case True:
                    match class_id:
                        case 2:
                            cop_yolo_res_img = simplify_polygon_k_with_dist(cop_yolo_res_img,options["NoP_Cars"])
                        case 3:
                            cop_yolo_res_img = simplify_polygon_k_with_dist(cop_yolo_res_img,options["NoP_Motorcycle"])
                        case 7:
                            cop_yolo_res_img = simplify_polygon_k_with_dist(cop_yolo_res_img,options["NoP_Truck"])
                        case _:
                            cop_yolo_res_img = simplify_polygon_k_with_dist(cop_yolo_res_img,options["NoP_other_Object"])

            case False:
                    match class_id:
                        case 2:
                            cop_yolo_res_img = simplify_polygon_k_with_angle(cop_yolo_res_img,options["NoP_Cars"])
                        case 3:
                            cop_yolo_res_img = simplify_polygon_k_with_angle(cop_yolo_res_img,options["NoP_Motorcycle"])
                        case 7:
                            cop_yolo_res_img = simplify_polygon_k_with_angle(cop_yolo_res_img,options["NoP_Truck"])
                        case _:
                            cop_yolo_res_img = simplify_polygon_k_with_angle(cop_yolo_res_img,options["NoP_other_Object"])
            case _:
                print("Error at 'calc_K_with_Dist' Options parameter; must be True or False!")
                return None        
    # print(len(cop_yolo_res_img))
    # print("/////////////////////////")
    # print(cop_yolo_res_img)
    return [cop_yolo_res_img]
        
        
    return [test]
   




def run_yolo(img, options):  #https://pysource.com/2023/02/21/yolo-v8-segmentation
    options["timestamp_yolo_start"] = time.time()
    ys = YOLOSegmentation("yolov8n-seg.pt")
    if(options["save_timestamps"]==True):
                options["timestamp_yolo_end"] = time.time()
                options["timestamp_yolo_dur"] = options["timestamp_yolo_dur"] + (options["timestamp_yolo_end"] - options["timestamp_yolo_start"])
    bboxes, classes, segmentations, scores = ys.detect(img)
   
    if(options["black_video"] == True):
        img_size = get_img_size(img)
        img = cv2.rectangle(img, (0,0),(img_size[0],img_size[1]), (0, 0, 0), -1)


    for bbox, class_id, seg, score in zip(bboxes, classes, segmentations, scores):
       
        (x, y, x2, y2) = bbox
        options["timestamp_DCE_start"] = time.time()
        outline = run_DCE([seg], class_id, options)
        if(options["save_timestamps"]==True):
                options["timestamp_DCE_end"] = time.time()
                options["timestamp_DCE_dur"] = options["timestamp_DCE_dur"] + (options["timestamp_DCE_end"] - options["timestamp_DCE_start"])
         
        options["timestamp_write_outline_start"] = time.time()
        cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), 2)

        cv2.polylines(img, outline, True, (255, 255, 255), 1)
      
        if(options["write_labels"] == True):
            img = cv2.putText(img, get_text_string(class_id,score), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        #cv2.putText(img, str(class_id), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        if(options["save_timestamps"]==True):
                options["timestamp_write_outline_end"] = time.time()
                options["timestamp_write_outline_dur"] = options["timestamp_write_outline_dur"] + (options["timestamp_write_outline_end"] - options["timestamp_write_outline_start"])
    return img

def get_text_string(class_id, score):
    category_list = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}
    category = category_list[class_id]
    return (category + str(score))   

def get_img_size(img):
    height, width, layers = img.shape
    img_size = [width, height]
    return img_size

def get_number_of_frames(path): #https://stackoverflow.com/questions/25359288/how-to-know-total-number-of-frame-in-a-file-with-cv2-in-python
    cap = cv2.VideoCapture(path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(length)
    return length

def get_fps(path):  #https://stackoverflow.com/questions/49025795/python-opencv-video-getcv2-cap-prop-fps-returns-0-0-fps
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    return fps


    
def get_specific_frame(path, frame_number): #https://stackoverflow.com/questions/33650974/opencv-python-read-specific-frame-using-videocapture
    if frame_number == 0:
        frame_number = 1
    cap = cv2.VideoCapture(path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number-1)
    res, frame = cap.read()
    #frame_resized = cv2.resize(frame, None, fx=1, fy=1)
    #cv2.imwrite(r'Code\YOLO\frames\raw\frame'+str(frame_number)+'.png', frame)  # save frame as JPEG file
    return frame


    
 
 
   


        

def analyse_vid(path):
    model = YOLO('yolov8n-seg.pt')
    results = model(path, save=False)
    return results



#test()