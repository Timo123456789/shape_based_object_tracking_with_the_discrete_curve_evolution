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
        outline = data_arr[2]
        scores = data_arr[3]
        print("_______________________________________________________________________________________________")
        print("bbox")
        print(data_arr[0])
        print(len(bbox))
        print("classid")
        print(data_arr[1])
        print("scores")
        print(data_arr[3])
        print("bbox1_start")
        print(bbox[0][0])
        print("bbox1_ende")
        print(bbox[0][1])
        print("_______________________________________________________________________________________________")
        res_cop[i]= cv2.polylines(res[i].orig_img, outline, True, (0, 0, 255), 1) #Hier kann DCE gut angewendet werden?
        for b in range(len(bbox)):
            res_cop[i] = cv2.rectangle(res_cop[i], (bbox[b][0],bbox[b][1]),(bbox[b][2],bbox[b][3]), (255, 0, 0), 2)
            if class_id[b] == 2: #car = 2,  motorcycle = 3, truck = 7,
                res_cop[i] = cv2.putText(res_cop[i], (str(class_id[b])+'car'), (bbox[b][0], bbox[b][1] - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else:
                if class_id[b] == 3:
                     res_cop[i] = cv2.putText(res_cop[i], (str(class_id[b])+'motorcycle'), (bbox[b][0], bbox[b][1] - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                else:
                    if class_id[b] == 7:
                         res_cop[i] = cv2.putText(res_cop[i], (str(class_id[b])+'truck'), (bbox[b][0], bbox[b][1] - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                    else:
                         res_cop[i] = cv2.putText(res_cop[i], str(class_id[b]), (bbox[b][0], bbox[b][1] - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        
       
        
    
    return res_cop




def get_data(res):
    segmentation_contours_idx = []
    # testimg = res.plot()
    # cv2.imshow("result", testimg)       
    # cv2.waitKey(0)
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