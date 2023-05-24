from ultralytics import YOLO
import cv2

def main():
    path = r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\yolov8_segmentation-pysource.com_\yolov8_segmentation-pysource.com\autobahn1s.mp4'
    path_write_video = r'Code\YOLO\runs\videos_from_frames\video_results.mp4'


    model = YOLO('yolov8n-seg.pt') 
    results_first = model.predict(path, save=False)
    print(results_first[3].masks)
    print("_______________________________________________________________________________________________")
    print(results_first[3].masks.xy)
    print(len(results_first))

    # testimg = results_first[1].plot()
    # cv2.imshow("result", testimg)       
    # cv2.waitKey(0)

    write_video(results_first, path_write_video)
   
    # https://github.com/ultralytics/yolov5/issues/9665  #ne Eher nicht ist pytorch






def write_video(res, path_write_video):
    height, width, layers = res[2].orig_img.shape
    fps = 33
    video=cv2.VideoWriter(path_write_video,-1,fps,(width,height))
    for i in range(fps):
        video.write(res[i].plot())
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