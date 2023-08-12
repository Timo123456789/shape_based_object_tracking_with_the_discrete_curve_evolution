from YOLO.yolo_result_version import *
from YOLO.yolo_every_frame import *
from Shape_Similiarity.shape_sim_meas import *
import cv2
import time




def main():
    """
    Main function that initializes an options dictionary at the beginning and then executes the respective YOLO version

    "yolo_every_frame" is an alternative YOLO implementation where the entire video is not immediately analyzed with YOLO. The video is first split into individual frames and then the YOLO algorithm is applied to each frame individually. This is more resource efficient and saves memory that would otherwise overflow. The disadvantage is that this method takes longer than applying YOLO directly to the entire video.

    __init__.py files are important for connecting DCE.py with yolo_every_frame.py and yolo_result_version.py
    """
    options = {
            "path_directory": r'Code\vid_examples\evaluation',  #main path for storing files
            "source_video": r'Code\vid_examples\evaluation\Autobahn5F.mp4', #name for source video
            "write_video": r'\newDCE_RV.mp4', #storing name for result video
            "results": r'\newDCE_RV_results.txt', # storing name for statistics

            "path_source_video": r'temp', #temp variable for storing path for source video
            "path_write_video": r'temp', #temp variable for storing path for write video
            "path_write_timestamps": r'temp', #temp variable for storing path for statistics txt

        	"NoP_Cars": 10, #Number of final Points for Cars
        	"NoP_Motorcycle": 5, #Number of final Points for Motorcycles
        	"NoP_Truck": 8, #Number of final Points for Trucks
        	"NoP_other_Object": 20, #Number of final Points for other Objects

            "YOLO_model": 'yolov8x-seg.pt',  #set YOLO Model
            "black_video": False, #Bool that turns the whole video black, so that only white sillhouettes are shown in the video
            "write_labels": True, #Bool that ensures that a label with scores is written to the video for each polygon
            "yolo_every_frame": False, #Boolean that enables an alternative YOLO application method

            "save_timestamps": True, #bool, which activates the saving of the timestamps
            "timestamp_prog_start": time.time(),
            "timestamp_prog_end": 0,
            "timestamp_yolo_start": 0,
            "timestamp_yolo_end": 0,
            "timestamp_yolo_dur": 0,
            "timestamp_write_outline_start": 0,
            "timestamp_write_outline_end": 0,
            "timestamp_write_outline_dur": 0,
            "timestamp_DCE_start": 0,
            "timestamp_DCE_end": 0,
            "timestamp_DCE_dur": 0,
            "timestamp_write_video_start": 0,
            "timestamp_write_video_end": 0,
            "timestamp_write_video_dur": 0,

            "angle_sums_polygons":[],
            "angle_sums_images":[],
            "shape_similarity_measure":-9.9999,
            "list_of_all_polygons":[],
            "list_of_polygons_in_one_frame":[],
            "number_of_polygons":0,
            "number_of_angles":0
    }
    options = setpaths(options)
 
    if (options["yolo_every_frame"] == True): #if clause to run selected YOLO Version
        run_yolo_every_frame_version(options)
    else:
        run_yolo_result_version(options)
   



def run_yolo_every_frame_version(options):
    """
    start YOLO Version, which splitted the video in every frame

    @param options: Dictionary with options set in main
    """
    run_yolo_every_frame_version_intern(options)

    calc_shape_similarity(options)

    return 0




def run_yolo_result_version(options):
    """
    start YOLO Version, which runs YOLO at the beginning

    @param options: Dictionary with options set in main
    """
    model = YOLO(options["YOLO_model"])
    options["timestamp_yolo_start"] = time.time()
    results = model.predict(options["path_source_video"], save=False) #init and run YOLO
    options["timestamp_yolo_end"] = time.time()

    options["timestamp_write_outline_start"] = time.time()
    res_outline = get_outline_for_every_object(results, options) #write outlines with DCE in result file
    options["timestamp_write_outline_end"] = time.time()

    options["timestamp_write_video_start"] = time.time()
    write_video(res_outline[0], options["path_write_video"], options["path_source_video"]) #saved video at the path in options variable
    options["timestamp_write_video_end"] = time.time()

    calc_shape_similarity(options)

    return 0







def setpaths(options):
    """
    set temp path variable in options files to exact paths in directory variable

    @param: options: Dictionary with options set in main
    """
    string_source_vid = options["source_video"]
    string_write_vid = options["path_directory"] + options["write_video"]
    string_timestamps = options["path_directory"] + options["results"]
    options["path_source_video"] = string_source_vid
    options["path_write_video"] = string_write_vid
    options["path_write_timestamps"] = string_timestamps
    return options




def run_test(options):
    # shape_similarity_val = 0
    # img_1 = get_specific_frame(options["path_source_video"],11)
    # img_2 = get_specific_frame(options["path_source_video"],15)
    # img_1_yolo = run_yolo(img_1, options, 11)
    # img_2_yolo = run_yolo(img_2, options, 15)
    # #img_1 = cv2.resize(img_1, fx = 0.5, fy = 0.5)
    # #img_2 = cv2.resize(img_2, fx = 0.5, fy = 0.5)
    # #print(options["list_of_all_polygons"])
    # polygon_array = options["list_of_all_polygons"]
    
    # temp = 0
  
    # for frame in range(len(polygon_array)-1):
    #     print(len(polygon_array[0]))
    #     print(polygon_array[0])
    #     for polygon in range(len(polygon_array[0])):
    #         temp = temp + (polygon_array[frame][polygon][2]-polygon_array[frame+1][polygon][2])
    # print("temp")            
    # print(temp)            
    # cv2.imshow("image", img_1)       
    # cv2.waitKey(0) 

    # print("shape_similarity_val")
    # print(shape_similarity_val)
    # cv2.imshow("image", img_1_yolo)       
    # cv2.waitKey(0) 
    # cv2.imshow("image", img_2_yolo)       
    # cv2.waitKey(0) 

    return 0




main()