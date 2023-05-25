
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