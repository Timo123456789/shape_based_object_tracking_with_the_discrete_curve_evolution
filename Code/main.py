from YOLO.yolo_result_version import *
from YOLO.yolo_every_frame import *
import cv2
import time




def main():
    """
    Main function that initializes an options dictionary at the beginning and then executes the respective YOLO version

    "calc_K_with_Dist" Bool: (ATTENTION!; currently still erroneous for small scores). Calculate K Value at DCE only with distances (according to Latecki, Lakämper, Wolter)

    "yolo_every_frame" is an alternative YOLO implementation where the entire video is not immediately analyzed with YOLO. The video is first split into individual frames and then the YOLO algorithm is applied to each frame individually. This is more resource efficient and saves memory that would otherwise overflow. The disadvantage is that this method takes longer than applying YOLO directly to the entire video.

    init.py files are important for connecting DCE.py with yolo_every_frame.py and yolo_result_version.py
    """
    options = {
            "path_source_video": r'Code\vid_examples\right_Side\autobahn1s.mp4',
            "path_write_video": r'Code\YOLO\runs\videos_from_frames\autobahn1s_temp.mp4',
            "path_write_timestamps": r'Code\YOLO\runs\videos_from_frames\timestamps_autobahn1s_temp_res_vers.txt',

        	"NoP_Cars": 7, #Number of final Points for Cars, first try: 10, second try: 25
        	"NoP_Motorcycle": 5, #Number of final Points for Motorcycles, first try: 5, second try: 20
        	"NoP_Truck": 8, #Number of final Points for Trucks, first try: 8, second try:45
        	"NoP_other_Object": 10, #Number of final Points for other Objects, first try: 20, second try:60

            "black_video": True, #Bool that turns the whole video black, so that only white sillhouettes are shown in the video
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
            "shape_similarity_measure":-9.9999
    }


    #run_test(options)
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
    model = YOLO('yolov8n-seg.pt') 
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




def calc_shape_similarity(options):
    """
    function that calculates the difference from the total angle sum of one image to the next. This difference is summed up and is the 'shape_similarity_measures'

    @param options: Dictionary with options set in main
    """
    shape_similarity_val = 0
    print(options["angle_sums_images"])
    print(len(options["angle_sums_images"]))
    for i in range(len(options["angle_sums_images"])-1):
         shape_similarity_val = shape_similarity_val +  options["angle_sums_images"][i] - options["angle_sums_images"][i+1]
    options["shape_similarity_measure"] = shape_similarity_val
    print("shape_similarity_measures calculated")



def save_timestamps_as_file_yolo_every_frame(options):
    """
    function to save timestamps when 'yolo_every_frame' is selected

    @param options: Dictionary with options set in main
    """
    f = open( options["path_write_timestamps"], 'w' )
    options["timestamp_prog_end"] = time.time()
    results = "Duration Program: " +ret_timestampline(options, "prog")+ '\n' +"Duration YOLO: " + str(round(options["timestamp_yolo_dur"],2))+" ms" +'\n'+"Duration write_Outline(exclude DCE Calculation) "+str(round((options["timestamp_write_outline_dur"]),2))+" ms" + '\n'+"Duration DCE: " +str(round(options["timestamp_DCE_dur"],2))+" ms" + '\n'+ "Duration write_video: """ + str(round((options["timestamp_write_video_dur"]),2))+ '\n'+ "Sum of individual variablels (must be the same as 'Duration Programm'): " +  str(round((options["timestamp_yolo_dur"]+options["timestamp_write_outline_dur"]+options["timestamp_DCE_dur"]+options["timestamp_write_video_dur"]),2)) + "sec." + '\n' + "Minimal deviations due to not exact timestamp setting" + '\n' + '\n' + "shape similarity measure (must be near 0): " + str(round(options["shape_similarity_measure"], 4)) + '\n' + "Total sum of the angles: " +str(round(sum(options["angle_sums_images"]),2)) + '\n' 
        
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
    results = "Duration Program: " +ret_timestampline(options, "prog")+ '\n' +"Duration YOLO: " +ret_timestampline(options, "yolo")+ '\n'+"Duration write_Outline(include DCE Calculation) "+str(round((options["timestamp_write_outline_end"]-options["timestamp_write_outline_start"]),2))+" ms" + '\n'+"Duration DCE: " +str(round(options["timestamp_DCE_dur"],2))+" ms" + '\n'+ "Duration write_video: """ +ret_timestampline(options, "write_video") + '\n'+ "Sum of individual variablels (must be the same as 'Duration Programm'): " +  str(round((options["timestamp_yolo_end"]-options["timestamp_yolo_start"])+(options["timestamp_write_outline_end"]-options["timestamp_write_outline_start"]-options["timestamp_DCE_dur"])+options["timestamp_DCE_dur"]+(options["timestamp_write_video_end"]-options["timestamp_write_video_start"]),2)) + "sec." + '\n' + "Minimal deviations due to not exact timestamp setting" + '\n' + '\n' + "shape similarity measure (must be near 0): " + str(round(options["shape_similarity_measure"], 4)) + '\n' + "Total sum of the angles: " +str(round(sum(options["angle_sums_images"]),2))
        
    f.write(str(results))
    print("timestamps saved")
    print("Processing Time:"+ ret_timestampline(options, "prog"))
    f.close()
    return 0




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
   




main()