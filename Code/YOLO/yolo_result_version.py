from ultralytics import YOLO
import cv2
import numpy as np

def main():
    path = r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\yolov8_segmentation-pysource.com_\yolov8_segmentation-pysource.com\autobahn1s.mp4'
    path_write_video = r'Code\YOLO\runs\videos_from_frames\video_results.mp4'


    model = YOLO('yolov8n-seg.pt') 
    results = model.predict(path, save=False)
    # print(results[3].boxes.xyxy)
    # print(results[3].boxes.xyxy[0])
    # print(np.array(results[3].boxes.xyxy.cpu(), dtype="int"))
    # detected_object_bbox = np.array(results[1].boxes.xyxy.cpu(), dtype="int")
    # print()
    # print("_______________________________________________________________________________________________")
    # print(results[3].masks.xy)

    # print("_______________________________________________________________________________________________")
    print(results[3].masks.xy)
    print(len(results))

    # testimg = results[10].plot()
    # cv2.imshow("result", testimg)       
    # cv2.waitKey(0)
    res_outline = get_outline_for_every_object(results)

    write_video(res_outline, path_write_video)
   
    # https://github.com/ultralytics/yolov5/issues/9665  #ne Eher nicht ist pytorch

def get_outline_for_every_object(res):
    fps = len(res)
    res_cop = res
    for i in range(fps):
        data_arr = get_data(res[i])
        bbox = data_arr[0]
        class_id = data_arr[1]
        outline = data_arr[2] #Hier kann DCE gut angewendet werden?
        scores = data_arr[3]
        res_cop[i]= cv2.polylines(res[i].orig_img, outline, True, (0, 0, 255), 1) 
        for b in range(len(bbox)):
            res_cop[i] = cv2.rectangle(res_cop[i], (bbox[b][0],bbox[b][1]),(bbox[b][2],bbox[b][3]), (255, 0, 0), 2)
            res_cop[i] = cv2.putText(res_cop[i], get_text_string(class_id[b],scores[b]), (bbox[b][0], bbox[b][1] - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
           
        
        
  
        
       
        
    
    return res_cop

def get_text_string(class_id, score):
    category_list = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}
    category = category_list[class_id]
    return (category + str(score))


def get_data(res):
    segmentation_contours_idx = []
    height, width, layers = res.orig_img.shape
    for seg in res.masks.segments:
        # contours
        seg[:, 0] *= width
        seg[:, 1] *= height
        segment = np.array(seg, dtype=np.int32)
        segmentation_contours_idx.append(segment)

    bboxes = np.array(res.boxes.xyxy.cpu(), dtype="int")
    # Get class ids
    class_ids = np.array(res.boxes.cls.cpu(), dtype="int")
    # Get scores
    scores = np.array(res.boxes.conf.cpu(), dtype="float").round(2)
    return bboxes, class_ids, segmentation_contours_idx, scores


def write_outline(img,arr):
    print(len(arr), arr.size)

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




def write_video(res, path_write_video):
    height, width, layers = res[2].shape
    fps = len(res)
    video=cv2.VideoWriter(path_write_video,-1,fps,(width,height))
    for i in range(fps):
        video.write(res[i])
    cv2.destroyAllWindows()
    video.release()
    print("video written")
    return 0



main()



# result = results_first

# height, width, channels = img.shape

#         results = self.model.predict(source=img.copy(), save=False, save_txt=False)
#         result = results[0]
#         segmentation_contours_idx = []
#         for seg in result.masks.segments:
#             # contours
#             seg[:, 0] *= width
#             seg[:, 1] *= height
#             segment = np.array(seg, dtype=np.int32)
#             segmentation_contours_idx.append(segment)

#         bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
#         # Get class ids
#         class_ids = np.array(result.boxes.cls.cpu(), dtype="int")
#         # Get scores
#         scores = np.array(result.boxes.conf.cpu(), dtype="float").round(2)
#         return bboxes, class_ids, segmentation_contours_idx, scores