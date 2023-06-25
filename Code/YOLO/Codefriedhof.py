
# def read_results_file(): 
#     f = open(r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\YOLO\temp\results.py')
#     contents = f.read()
#     return contents


# def write_results_file(results):
#     f = open( r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\YOLO\temp\results.py', 'w' )
#     f.write(repr(results))
#     f.close()
    
# def read_results_file_pickle():
#     # f = open(r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\YOLO\temp\results.py')
#     # f = open(r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\results_panda.txt')
#     contents = pandas.read_pickle(r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\results_panda.py')
#     return (contents)

# def write_results_file_pickle(results):
   
#     file_name = 'results_panda.py'
#     with open(file_name, 'wb') as file:
#         pandas.to_pickle(results, file, compression={'method': 'gzip', 'compresslevel': 1, 'mtime': 1})
#         print(f'Object successfully saved to "{file_name}"')



    #Schreibe und lese Ergebnisse in File
    #write_results_file_pickle(results)
    # write_results_file(results)
    #mit Pickle
  
    #result_pickle = read_results_file_pickle()

    #ohne pickle
 
    # result_txt = read_results_file()

    # #print(result_pickle)
    # print("________________________________________________________________________________________________________________")
    # print("________________________________________________________________________________________________________________")
    # #print(raw_results[0].masks)
    # print("________________________________________________________________________________________________________________")



   # print(result)
    # height, width, channels = img.shape
    # segmentation_contours_idx = []
    # for seg in result.masks.segments:
    #         # contours
    #         seg[:, 0] *= width
    #         seg[:, 1] *= height
    #         segment = np.array(seg, dtype=np.int32)
    #         segmentation_contours_idx.append(segment)

    #     bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
    #     # Get class ids
    #     class_ids = np.array(result.boxes.cls.cpu(), dtype="int")
    #     # Get scores
    #     scores = np.array(result.boxes.conf.cpu(), dtype="float").round(2)
    #     return bboxes, class_ids, segmentation_contours_idx, scores




# def getFirstFrame(videofile):  #https://python-forum.io/thread-13999.html

#     """
#     KANN EIGENTLICH GELÖSCHT WERDEN!!!!
#     """
#     vidcap = cv2.VideoCapture(videofile)
#     success, image = vidcap.read()
#     if success:
#         cv2.imwrite(r"Code\YOLO\frames\first_frame.jpg", image)  # save frame as JPEG file
#         return image


    # testimg = cv2.imread(r'Code\YOLO\frames\analyzed\frame2.png')
    # cv2.imshow("image", testimg)       
    # cv2.waitKey(0) 

   # for i in range(framecounter):
    #     img_arr.append(cv2.imread(path_read_imgs+str(i)+'.png'))
    #     #cv2.imshow("image", img_arr[i])
    # print(img_arr)




# def create_segments(res):
#     print(res)
#     fps = len(res)
#     for i in range(fps):
#         detected_object_bbox = np.array(res[i].boxes.xyxy.cpu(), dtype="int")
#         for x in range(len(detected_object_bbox)):
#             x1 = detected_object_bbox[x][0]
#             y1 = detected_object_bbox[x][1]
            
#             x2 = detected_object_bbox[x][2]
#             y2 = detected_object_bbox[x][3]
#             res[i] = cv2.rectangle(res[i].orig_img, (x1,y1),(x2,y2),(255, 0, 0), 2)   #https://stackoverflow.com/questions/75324341/yolov8-get-predicted-bounding-box
#         #
   
#     return res



#  if class_id[b] == 2: #car = 2,  motorcycle = 3, truck = 7,
#                 res_cop[i] = cv2.putText(res_cop[i], (str(class_id[b])+'car'), (bbox[b][0], bbox[b][1] - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
#             else:
#                 if class_id[b] == 3:
#                      res_cop[i] = cv2.putText(res_cop[i], (str(class_id[b])+'motorcycle'), (bbox[b][0], bbox[b][1] - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
#                 else:
#                     if class_id[b] == 7:
#                          res_cop[i] = cv2.putText(res_cop[i], (str(class_id[b])+'truck'), (bbox[b][0], bbox[b][1] - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
#                     else:
#                          res_cop[i] = cv2.putText(res_cop[i], str(class_id[b]), (bbox[b][0], bbox[b][1] - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)


# def run_yolo_new(img):  #https://pysource.com/2023/02/21/yolo-v8-segmentation
#     ys = YOLOSegmentation("yolov8n-seg.pt")
#     #bboxes, classes, segmentations, pixels, scores = ys.detect(img)
#     #bboxes, classes, segmentations, pixels, scores = ys.detect(img)
#     # print("test")
#     # for bbox, class_id, seg, px, score in zip(bboxes, classes, segmentations, pixels, scores):
#     #     # print("bbox:", bbox, "class id:", class_id, "seg:", seg, "score:", score)
#     #     print("HALO", score)
#     #     (x, y, x2, y2) = bbox
#     #     # match class_id:
#     #     #     case 2:
#     #     # if class_id == 2 or class_id == 3 or class_id == 7:  #car = 2,  motorcycle = 3, truck = 7,
#     #     print("ID")
#     #     cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), 2)
#     #     #cv2.polylines(img, run_DCE([seg],class_id), True, (0, 0, 255), 1)
#     #     cv2.polylines(img, run_DCE(px, class_id, seg), True, (0, 0, 255), 10)
#     #     #cv2.polylines(img, [seg], True, (0, 0, 255), 1)

#     #     cv2.putText(img, str(class_id), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
#     # print("Test Ende")

#     bboxes, classes, segmentations, scores = ys.detect(img)
#     for bbox, class_id, seg, score in zip(bboxes, classes, segmentations, scores):
#         # print("bbox:", bbox, "class id:", class_id, "seg:", seg, "score:", score)
#         (x, y, x2, y2) = bbox
#         print("test5")
#         if class_id == 32:
#             cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), 2)

#             cv2.polylines(img, [seg], True, (0, 0, 255), 4)

#             cv2.putText(img, str(class_id), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
#     return img




# def calc_remaining_points(NoP, class_id, options):
#     match class_id:
#         case 2:
#             return NoP - options["NoP_Cars"]
#         case 3:
#             return NoP - options["NoP_Motorcycle"]
#         case 7: 
#             return NoP - options["NoP_Truck"]
#         case _:
#             return NoP - options["NoP_other_Object"]

#test for calc shape similarity measure:

# def run_test(options):
#     shape_similarity_val = 0
#     img_1 = get_specific_frame(options["path_source_video"],11)
#     img_2 = get_specific_frame(options["path_source_video"],15)
#     img_1_yolo = run_yolo(img_1, options)
#     img_2_yolo = run_yolo(img_2, options)
#     #img_1 = cv2.resize(img_1, fx = 0.5, fy = 0.5)
#     #img_2 = cv2.resize(img_2, fx = 0.5, fy = 0.5)

#     # cv2.imshow("image", img_1)       
#     # cv2.waitKey(0) 
#     # cv2.imshow("image", img_2)       
#     # cv2.waitKey(0) 

    
#     # cv2.imshow("image", img_1_yolo)       
#     # cv2.waitKey(0) 
#     # print(options["angle_sums_polygons"])
#     # print(len(options["angle_sums_polygons"]))
  
#     # print(len(options["angle_sums_polygons"]))
#     print(options["angle_sums_images"])
#     print(len(options["angle_sums_images"]))

#     for i in range(len(options["angle_sums_images"])-1):
#         shape_similarity_val +=  options["angle_sums_images"][i] - options["angle_sums_images"][i+1]

#     print("shape_similarity_val")
#     print(shape_similarity_val)
#     cv2.imshow("image", img_1_yolo)       
#     cv2.waitKey(0) 
#     cv2.imshow("image", img_2_yolo)       
#     cv2.waitKey(0) 

#     return 0


#Testfunction for yolo result version
# def test():
#     """
#     testfunction for yolo_result_version.py; 
#     use only when you would run yolo_result_version.py without main.py

#     write some testdata
#     """ 
#     path_source_video = r'Code\vid_examples\right_Side\autobahn1s.mp4'
#     path_write_video = r'Code\YOLO\runs\video_temp.mp4'


#     model = YOLO('yolov8n-seg.pt') 
#     results = model.predict(path_source_video, save=False)
 
#     res_outline = get_outline_for_every_object(results)

#     write_video(res_outline, path_write_video, path_source_video)




# #test()





#Testfunction for yolo every frame version
# def test(): 
#     """
#     testfunction for yolo_every_frame.py; 
#     use only when you would run yolo_every_frame.py without main.py

#     write some testdata
#     """ 
#     #path_source_video = r'Code\vid_examples\right_Side\autobahn_2.mp4'
#     path_source_video = r'Code\vid_examples\right_Side\autobahn_2.mp4'
#     path_read_imgs = r'Code\YOLO\frames\analyzed\frame'
#     path_write_video = r'Code\YOLO\runs\videos_from_frames\videotest_9.mp4'
#     # 8n = sehr schnell, aber ungenau, 8m = schnell recht genau, 8x = langsam aber sehr genau

#     framecounter = get_number_of_frames(path_source_video)
#     fps = get_fps(path_source_video)
#     print("framecounter")
#     print(framecounter)

#     print("fps")
#     print(fps)
#     img_arr=[]
    
#     for i in range(framecounter):
#         img = get_specific_frame(path_source_video,i)
#         img_analyzed = run_yolo(img)
#         img_arr.append(img_analyzed)
        
#         #cv2.imwrite(r'Code\YOLO\frames\analyzed\frame'+str(i)+'.png', img_analyzed)  # save frame as JPEG file
#     create_video_from_imgs(path_source_video,path_write_video,img_arr, framecounter)




# #test()
