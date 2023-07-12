from YOLO.yolo_result_version import *
from YOLO.yolo_every_frame import *
from Shape_Similiarity.shape_sim_meas import *
import cv2
import time




def main():
    """
    Main function that initializes an options dictionary at the beginning and then executes the respective YOLO version

    "yolo_every_frame" is an alternative YOLO implementation where the entire video is not immediately analyzed with YOLO. The video is first split into individual frames and then the YOLO algorithm is applied to each frame individually. This is more resource efficient and saves memory that would otherwise overflow. The disadvantage is that this method takes longer than applying YOLO directly to the entire video.

    init.py files are important for connecting DCE.py with yolo_every_frame.py and yolo_result_version.py
    """
    options = {
            "path_source_video": r'Code\vid_examples\autobahn_long_shot_135s.mp4',
            "path_write_video": r'Code\YOLO\runs\autobahn_ls_135_ev_vers.mp4',
            "path_write_timestamps": r'Code\YOLO\runs\timestamps_autobahn_ls_135_ev_vers.txt',

        	"NoP_Cars": 10, #Number of final Points for Cars, first try: 10, second try: 25
        	"NoP_Motorcycle": 5, #Number of final Points for Motorcycles, first try: 5, second try: 20
        	"NoP_Truck": 8, #Number of final Points for Trucks, first try: 8, second try:45
        	"NoP_other_Object": 20, #Number of final Points for other Objects, first try: 20, second try:60

            "YOLO_model": 'yolov8n-seg.pt',  #set YOLO Model
            "black_video": True, #Bool that turns the whole video black, so that only white sillhouettes are shown in the video
            "write_labels": True, #Bool that ensures that a label with scores is written to the video for each polygon
            "yolo_every_frame": True, #Boolean that enables an alternative YOLO application method

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
    
    if(options["save_timestamps"]==True): #if clause to save the timestamps
        if (options["yolo_every_frame"]== True):
            save_timestamps_as_file_yolo_every_frame(options)
        else:
            return 0
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

    if(options["save_timestamps"]==True): #if clause to save the timestamps
        save_timestamps_as_file_yolo_result(options)
    return 0




def save_timestamps_as_file_yolo_every_frame(options):
    """
    function to save timestamps when 'yolo_every_frame' is selected

    @param options: Dictionary with options set in main
    """
    f = open( options["path_write_timestamps"], 'w' )
    options["timestamp_prog_end"] = time.time()
    results = "Duration Program: " +ret_timestampline(options, "prog")+ '\n' +"Duration YOLO: " + str(round(options["timestamp_yolo_dur"],2))+" ms" +'\n'+"Duration write_Outline(exclude DCE Calculation) "+str(round((options["timestamp_write_outline_dur"]),2))+" ms" + '\n'+"Duration DCE: " +str(round(options["timestamp_DCE_dur"],2))+" ms" + '\n'+ "Duration write_video: """ + str(round((options["timestamp_write_video_dur"]),2))+ '\n'+ "Sum of individual variablels (must be the same as 'Duration Programm'): " +  str(round((options["timestamp_yolo_dur"]+options["timestamp_write_outline_dur"]+options["timestamp_DCE_dur"]+options["timestamp_write_video_dur"]),2)) + "sec." + '\n' + "Minimal deviations due to not exact timestamp setting" + '\n' + '\n' + "shape similarity measure (must be near 0): " + str(round(options["shape_similarity_measure"], 4)) + '\n' +calc_procent_deviation(options)+ '\n' + "Total sum of the angles: " +str(round(sum(options["angle_sums_images"]),2)) +'\n' 
        
    f.write(str(results))
    print("timestamps saved")
    print("Processing Time:"+ ret_timestampline(options, "prog"))
    f.close()
    return 0




def save_timestamps_as_file_yolo_result(options):
    """
    function to save timestamps when 'yolo_result_version' is selected

    @param options: Dictionary with options set in main
    """
    f = open( options["path_write_timestamps"], 'w' )
    options["timestamp_prog_end"] = time.time()
    results = "Duration Program: " +ret_timestampline(options, "prog")+ '\n' +"Duration YOLO: " +ret_timestampline(options, "yolo")+ '\n'+"Duration write_Outline(include DCE Calculation) "+str(round((options["timestamp_write_outline_end"]-options["timestamp_write_outline_start"]),2))+" ms" + '\n'+"Duration DCE: " +str(round(options["timestamp_DCE_dur"],2))+" ms" + '\n'+ "Duration write_video: """ +ret_timestampline(options, "write_video") + '\n'+ "Sum of individual variablels (must be the same as 'Duration Programm'): " +  str(round((options["timestamp_yolo_end"]-options["timestamp_yolo_start"])+(options["timestamp_write_outline_end"]-options["timestamp_write_outline_start"]-options["timestamp_DCE_dur"])+options["timestamp_DCE_dur"]+(options["timestamp_write_video_end"]-options["timestamp_write_video_start"]),2)) + "sec." + '\n' + "Minimal deviations due to not exact timestamp setting" + '\n' + '\n' + "shape similarity measure (must be near 0): " + str(round(options["shape_similarity_measure"], 4)) + '\n'+ calc_procent_deviation(options) + '\n' + "Total sum of the angles: " +str(round(sum(options["angle_sums_images"]),2)) +'\n' 
        
    f.write(str(results))
    print("timestamps saved")
    print("Processing Time:"+ ret_timestampline(options, "prog"))
    f.close()
    return 0




def calc_procent_deviation(options):
    """
    calculate the procent deviation and return this as string

    @param options: Dictionary with options set in main
    @return string
    """
    G = sum(options["angle_sums_images"]) #ground value
    W = options["shape_similarity_measure"]
    p = (W/G)*100
    value = round(p, 4)
    if value < 0:
        value = value*-1        
    string = "Percent Deviation: " +str(value) + " %"
    return string




def ret_timestampline(options, string):
    """
    function that returns a timestamp string; transform timestamps to ms and minutes 

    @param options: Dictionary with options 
    @param string: Value for given options variable 
    @return string
    """
    time_in_ms = round((options["timestamp_"+string+"_end"]-options["timestamp_"+string+"_start"]) * 100, 2)
    time_in_s = round((time_in_ms /100), 2)
    time_in_min = round((time_in_s/60),2)
    if (time_in_s > 180):
        return str(time_in_ms) +" ms / "+str(time_in_s)+" sec /" + str(time_in_min)+" min," 
    else:
        return str(time_in_ms) +" ms / "+str(time_in_s)+" sec," 




def run_test(options):
    shape_similarity_val = 0
    img_1 = get_specific_frame(options["path_source_video"],11)
    img_2 = get_specific_frame(options["path_source_video"],15)
    img_1_yolo = run_yolo(img_1, options, 11)
    img_2_yolo = run_yolo(img_2, options, 15)
    #img_1 = cv2.resize(img_1, fx = 0.5, fy = 0.5)
    #img_2 = cv2.resize(img_2, fx = 0.5, fy = 0.5)
    #print(options["list_of_all_polygons"])
    polygon_array = options["list_of_all_polygons"]
    print(polygon_array)
    print(polygon_array[0][0][2])
    print(polygon_array[1][0][2])
    print("  ")
    print(polygon_array[0][0])
    print(polygon_array[1][0])
    
    temp = 0
  
    for frame in range(len(polygon_array)-1):
        print(len(polygon_array[0]))
        print(polygon_array[0])
        for polygon in range(len(polygon_array[0])):
            temp = temp + (polygon_array[frame][polygon][2]-polygon_array[frame+1][polygon][2])
    print("temp")            
    print(temp)            
    cv2.imshow("image", img_1)       
    cv2.waitKey(0) 
    # cv2.imshow("image", img_2)       
    # cv2.waitKey(0) 

    
    # cv2.imshow("image", img_1_yolo)       
    # cv2.waitKey(0) 
    # print(options["angle_sums_polygons"])
    # print(len(options["angle_sums_polygons"]))
  
    # print(len(options["angle_sums_polygons"]))
    print(options["angle_sums_images"])
    print(len(options["angle_sums_images"]))



    # for i in range(len(options["angle_sums_images"])-1):
    #     shape_similarity_val +=  options["angle_sums_images"][i] - options["angle_sums_images"][i+1]

    print("shape_similarity_val")
    print(shape_similarity_val)
    cv2.imshow("image", img_1_yolo)       
    cv2.waitKey(0) 
    cv2.imshow("image", img_2_yolo)       
    cv2.waitKey(0) 

    return 0





main()