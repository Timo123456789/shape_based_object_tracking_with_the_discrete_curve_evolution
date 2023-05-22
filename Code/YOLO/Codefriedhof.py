
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