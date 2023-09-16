"""
Main File for a prototypical implemenation for the combination of "You Only Look Once" (YOLO) (Redmon, 2016, doi: 10.1109/CVPR.2016.91 ) (Vers. YOLOv8x, Ultralytics, 2023) and Discrete Curce Evolution (DCE) (Latecki, 1999, doi: 10.1006/cviu.1998.0738 ); based on hypothesis by Dorr, Latecki and  Moratz (2015, doi: 10.1007/978-3-319-23374-1_7 )

Must be used with the files: DCE.py, yolo_every_frame.py, yolo_result_version.py, yolo_segementation.py, shape_sim_meas.py 

Implementation for bachelor thesis: "Formbasiertes Objekttracking mit der Discrete Curve Evolution"
                                    "Shape-based object tracking with the Discrete Curve Evolution" 

                                    at Westfaelische Wilhelms Universitaet Muenster
                                    First Supervisor: Prof. Dr. Ing. Reinhard Moratz
                                    Second Supervisor: Dr. Christian Knoth

@author: Timo Lietmeyer, 11.09.2023
@contact: timolietmeyer@uni-muenster.de (for question, etc.)

supported by Vocavit GmbH, Hamburg

"""
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
            "path_directory": r'Code\vid_examples\evaluation\weitere_testfaelle\longshots',  #main path for storing files
            "source_video": r'Code\vid_examples\evaluation\Autobahn60s.mp4', #name for source video
            "write_video": r'\A60s_RV.mp4', #storing name for result video
            "results": r'\A60s_RV_results.txt', # storing name for statistics

            "path_source_video": r'temp', #temp variable for storing path for source video
            "path_write_video": r'temp', #temp variable for storing path for write video
            "path_write_timestamps": r'temp', #temp variable for storing path for statistics txt

        	"NoP_Cars": 20, #Number of final Points for Cars #bei 6 recht hohe Spruenge, 8 passt gut
        	"NoP_Motorcycle": 20, #Number of final Points for Motorcycles
        	"NoP_Truck": 20, #Number of final Points for Trucks #11 P ist vllt ideal
        	"NoP_other_Object": 20, #Number of final Points for other Objects

            "YOLO_model": 'yolov8x-seg.pt',  #set YOLO Model
            "black_video": False, #Bool that turns the whole video black, so that only white sillhouettes are shown in the video
            "black_bboxes": True, #Bool that turns the bounding boxes for detected objects black; overwritten by black_video variable
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
            "number_of_angles":0,
            "number_of_angles_bef_DCE":0,
            "number_of_compared_angles":0
    }
    options = setpaths(options)
 
    if (options["yolo_every_frame"] == True): #if clause to run selected YOLO Version
        run_yolo_every_frame_version(options)
    else:
        run_yolo_result_version(options)
    print("sucessfully stopped")




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
    """
    function to test different things at an example video

    @param options: Dictionary with options set in main
    """
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




def run_evaluation():
    """
    function, to run different evaluation videos; 12 videostreams with different settings for YOLO  Implementation Version; Length and YOLO Model
    """
    #YOLO V8n, Selected YOLO Version
    options = set_options_on_default() #set options dicitonary to default values
    options["path_directory"] = r'Code\vid_examples\evaluation\01Yolo8n' #select path directory where the files would be saved
    options["source_video"] = r'Code\vid_examples\evaluation\Autobahn1s.mp4' #select source video
    options["write_video"] = r'\A1s_EF_vers.mp4' #select name for written video
    options["results"] = r'\A1s_EF_results.txt' #select name for written statistics file
    options["YOLO_model"] = "yolov8n-seg.pt" #select YOLO Model
    options["yolo_every_frame"] = True #select YOLO implementation version
    run_test_case(options)

    options = set_options_on_default() #similar to case above; minor changes
    options["path_directory"] = r'Code\vid_examples\evaluation\01Yolo8n'
    options["source_video"] = r'Code\vid_examples\evaluation\Autobahn1s.mp4'
    options["write_video"] = r'\A1s_RV.mp4'
    options["results"] = r'\A1s_RV_results.txt'
    options["YOLO_model"] = "yolov8n-seg.pt"
    options["yolo_every_frame"] = False
    run_test_case(options)

    options = set_options_on_default() #similar to first case; minor changes
    options["path_directory"] = r'Code\vid_examples\evaluation\01Yolo8n'
    options["source_video"] = r'Code\vid_examples\evaluation\Autobahn10s.mp4'
    options["write_video"] = r'\A10s_EF_vers.mp4'
    options["results"] = r'\A10s_EF_results.txt'
    options["YOLO_model"] = "yolov8n-seg.pt"
    options["yolo_every_frame"] = True
    run_test_case(options)

    options = set_options_on_default() #similar to first case; minor changes
    options["path_directory"] = r'Code\vid_examples\evaluation\01Yolo8n'
    options["source_video"] = r'Code\vid_examples\evaluation\Autobahn10s.mp4'
    options["write_video"] = r'\A10s_RV.mp4'
    options["results"] = r'\A10s_RV_results.txt'
    options["YOLO_model"] = "yolov8n-seg.pt"
    options["yolo_every_frame"] = False
    run_test_case(options)



    #YOLO V8m
    options = set_options_on_default() #similar to first case; minor changes
    options["path_directory"] = r'Code\vid_examples\evaluation\02Yolo8m'
    options["source_video"] = r'Code\vid_examples\evaluation\Autobahn1s.mp4'
    options["write_video"] = r'\A1s_EF_vers.mp4'
    options["results"] = r'\A1s_EF_results.txt'
    options["YOLO_model"] = "yolov8m-seg.pt"
    options["yolo_every_frame"] = True
    run_test_case(options)

    options = set_options_on_default() #similar to first case; minor changes
    options["path_directory"] = r'Code\vid_examples\evaluation\02Yolo8m'
    options["source_video"] = r'Code\vid_examples\evaluation\Autobahn1s.mp4'
    options["write_video"] = r'\A1s_RV.mp4'
    options["results"] = r'\A1s_RV_results.txt'
    options["YOLO_model"] = "yolov8m-seg.pt"
    options["yolo_every_frame"] = False
    run_test_case(options)

    options = set_options_on_default() #similar to first case; minor changes
    options["path_directory"] = r'Code\vid_examples\evaluation\02Yolo8m'
    options["source_video"] = r'Code\vid_examples\evaluation\Autobahn10s.mp4'
    options["write_video"] = r'\A10s_EF_vers.mp4'
    options["results"] = r'\A10s_EF_results.txt'
    options["YOLO_model"] = "yolov8m-seg.pt"
    options["yolo_every_frame"] = True
    run_test_case(options)

    options = set_options_on_default() #similar to first case; minor changes
    options["path_directory"] = r'Code\vid_examples\evaluation\02Yolo8m'
    options["source_video"] = r'Code\vid_examples\evaluation\Autobahn10s.mp4'
    options["write_video"] = r'\A10s_RV.mp4'
    options["results"] = r'\A10s_RV_results.txt'
    options["YOLO_model"] = "yolov8m-seg.pt"
    options["yolo_every_frame"] = False
    run_test_case(options)



    #Yolo V8x
    options = set_options_on_default() #similar to first case; minor changes
    options["path_directory"] = r'Code\vid_examples\evaluation\03Yolo8x'
    options["source_video"] = r'Code\vid_examples\evaluation\Autobahn1s.mp4'
    options["write_video"] = r'\A1s_EF_vers.mp4'
    options["results"] = r'\A1s_EF_results.txt'
    options["YOLO_model"] = "yolov8x-seg.pt"
    options["yolo_every_frame"] = True
    run_test_case(options)

    options = set_options_on_default() #similar to first case; minor changes
    options["path_directory"] = r'Code\vid_examples\evaluation\03Yolo8x'
    options["source_video"] = r'Code\vid_examples\evaluation\Autobahn1s.mp4'
    options["write_video"] = r'\A1s_RV.mp4'
    options["results"] = r'\A1s_RV_results.txt'
    options["YOLO_model"] = "yolov8x-seg.pt"
    options["yolo_every_frame"] = False
    run_test_case(options)

    options = set_options_on_default() #similar to first case; minor changes
    options["path_directory"] = r'Code\vid_examples\evaluation\03Yolo8x'
    options["source_video"] = r'Code\vid_examples\evaluation\Autobahn10s.mp4'
    options["write_video"] = r'\A10s_EF_vers.mp4'
    options["results"] = r'\A10s_EF_results.txt'
    options["YOLO_model"] = "yolov8x-seg.pt"
    options["yolo_every_frame"] = True
    run_test_case(options)

    options = set_options_on_default() #similar to first case; minor changes
    options["path_directory"] = r'Code\vid_examples\evaluation\03Yolo8x'
    options["source_video"] = r'Code\vid_examples\evaluation\Autobahn10s.mp4'
    options["write_video"] = r'\A10s_RV.mp4'
    options["results"] = r'\A10s_RV_results.txt'
    options["YOLO_model"] = "yolov8x-seg.pt"
    options["yolo_every_frame"] = False
    run_test_case(options)

    return 0




def run_test_case(options):
    """
    run a test case with the in the options setted variables

    @param options: Dictionary with options set in main
    """
    options = setpaths(options)
 
    if (options["yolo_every_frame"] == True): #if clause to run selected YOLO Version
        run_yolo_every_frame_version(options)
    else:
        run_yolo_result_version(options)




def set_options_on_default():
     """
     setted the options variable to the default values

     @return options: Dictionary     
     """
     options = {
            "path_directory": r'temp',  #main path for storing files
            "source_video": r'temp', #name for source video
            "write_video": r'temp', #storing name for result video
            "results": r'temp', # storing name for statistics

            "path_source_video": r'temp', #temp variable for storing path for source video
            "path_write_video": r'temp', #temp variable for storing path for write video
            "path_write_timestamps": r'temp', #temp variable for storing path for statistics txt

        	"NoP_Cars": 8, #Number of final Points for Cars
        	"NoP_Motorcycle": 5, #Number of final Points for Motorcycles
        	"NoP_Truck": 11, #Number of final Points for Trucks
        	"NoP_other_Object": 20, #Number of final Points for other Objects

            "YOLO_model": 'yolov8n-seg.pt',  #set YOLO Model
            "black_video": True, #Bool that turns the whole video black, so that only white sillhouettes are shown in the video
            "black_bboxes": True, #Bool that turns the bounding boxes for detected objects black; overwritten by black_video variable
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
            "number_of_angles":0,
            "number_of_angles_bef_DCE":0,
            "number_of_compared_angles":0
    }
     return options




#run_evaluation()
main()