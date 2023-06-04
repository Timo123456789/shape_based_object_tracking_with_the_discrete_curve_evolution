#codesource: https://towardsdatascience.com/enhanced-object-detection-how-to-effectively-implement-yolov8-afd1bf6132ae

from ultralytics import YOLO
import pandas # Source: https://java2blog.com/save-object-to-file-python/
import numpy as np
import cv2
from yolo_segmentation import YOLOSegmentation



#masks2segment example : https://stackoverflow.com/questions/75545012/yolov8-segmentation-mask-problem-masks-looks-2-parts-but-outputs-only-first-par



def test(): 
    path_source_video = r'Code\vid_examples\right_Side\autobahn_2.mp4'
    path_read_imgs = r'Code\YOLO\frames\analyzed\frame'
    path_write_video = r'Code\YOLO\runs\videos_from_frames\video.mp4'
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



   
  


def create_video_from_imgs(path_source_video,path_write_video, img_arr, framecounter): #https://stackoverflow.com/questions/43048725/python-creating-video-from-images-using-opencv
    height, width, layers = get_specific_frame(path_source_video, (framecounter)).shape
    fps = get_fps(path_source_video)
    video=cv2.VideoWriter(path_write_video,-1,fps,(width,height))
    for i in range(framecounter):
        video.write(img_arr[i])
    cv2.destroyAllWindows()
    video.release()
    return 0
    
 
    

 
        

  
    
def run_DCE(array, class_id):
    #print(array)

    return array
   

def run_yolo(img):  #https://pysource.com/2023/02/21/yolo-v8-segmentation
    ys = YOLOSegmentation("yolov8n-seg.pt")
    bboxes, classes, segmentations, scores = ys.detect(img)
    for bbox, class_id, seg, score in zip(bboxes, classes, segmentations, scores):
        # print("bbox:", bbox, "class id:", class_id, "seg:", seg, "score:", score)
        (x, y, x2, y2) = bbox
        if class_id == 2 or class_id == 3 or class_id == 7:  #car = 2,  motorcycle = 3, truck = 7,
            cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), 2)

            cv2.polylines(img, run_DCE([seg],class_id), True, (0, 0, 255), 1)

            cv2.putText(img, str(class_id), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    return img


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
    frame_resized = cv2.resize(frame, None, fx=0.5, fy=0.5)
    #cv2.imwrite(r'Code\YOLO\frames\raw\frame'+str(frame_number)+'.png', frame)  # save frame as JPEG file
    return frame_resized


    
 
 
   


        

def analyse_vid(path):
    model = YOLO('yolov8n-seg.pt')
    results = model(path, save=False)
    return results



test()