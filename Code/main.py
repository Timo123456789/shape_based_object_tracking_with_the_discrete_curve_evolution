from YOLO.yolo_result_version import *
from YOLO.yolo_every_frame import *
import time
#from DCE.DCE import * 


def main():
    #path_source_video = r'Code\vid_examples\left_Side\not_stabilized\autobahn_6.mp4'
    #path_source_video = r'Code\vid_examples\right_Side\autobahn1s.mp4'
   # path_write_video = r'Code\YOLO\runs\videos_from_frames\autobahn_xy_temp.mp4'
    options = {
            #"path_source_video": r'Code\vid_examples\left_Side\not_stabilized\autobahn_6.mp4',
            "path_source_video": r'Code\vid_examples\right_Side\autobahn1s.mp4',
            "path_write_video": r'Code\YOLO\runs\videos_from_frames\autobahn1s_temp.mp4',
            "path_write_timestamps": r'Code\YOLO\runs\videos_from_frames\timestamps_every_frame.txt',

        	"NoP_Cars": 10, #Number of final Points for Cars, first try: 10, second try: 25
        	"NoP_Motorcycle": 5, #Number of final Points for Motorcycles, first try: 5, second try: 20
        	"NoP_Truck": 8, #Number of final Points for Trucks, first try: 8, second try:45
        	"NoP_other_Object": 20, #Number of final Points for other Objects, first try: 20, second try:60

            "black_video": True,
            "write_labels": True,
            "calc_K_with_Dist": False,
            "yolo_every_frame": False,

            "save_timestamps": True,
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
            "timestamp_write_video_dur": 0

    }
    #run_yolo_result_version(options)
    print(options["timestamp_prog_start"])

   
    if (options["yolo_every_frame"] == True):
        run_yolo_every_frame_version(options)
    else:
        run_yolo_result_version(options)

   
def run_yolo_every_frame_version(options):
    run_yolo_every_frame_version_intern(options)

    if(options["save_timestamps"]==True):
        if (options["yolo_every_frame"]== True):
            save_timestamps_as_file_yolo_every_frame(options)
        else:
            save_timestamps_as_file(options)
    return 0



def run_yolo_result_version(options):
    model = YOLO('yolov8n-seg.pt') 
    options["timestamp_yolo_start"] = time.time()
    results = model.predict(options["path_source_video"], save=False)
    options["timestamp_yolo_end"] = time.time()

    options["timestamp_write_outline_start"] = time.time()
    res_outline = get_outline_for_every_object(results, options)
    options["timestamp_write_outline_end"] = time.time()

    options["timestamp_write_video_start"] = time.time()
    write_video(res_outline[0], options["path_write_video"], options["path_source_video"])
    options["timestamp_write_video_end"] = time.time()

    if(options["save_timestamps"]==True):
        save_timestamps_as_file(options)
    return 0

def save_timestamps_as_file_yolo_every_frame(options):
    f = open( options["path_write_timestamps"], 'w' )
    options["timestamp_prog_end"] = time.time()
    results = "Duration Program: " +ret_timestampline(options, "prog")+ '\n' +"Duration YOLO: " + str(round(options["timestamp_yolo_dur"],2))+" ms" +'\n'+"Duration write_Outline(exclude DCE Calculation) "+str(round((options["timestamp_write_outline_dur"]),2))+" ms" + '\n'+"Duration DCE: " +str(round(options["timestamp_DCE_dur"],2))+" ms" + '\n'+ "Duration write_video: """ + str(round((options["timestamp_write_video_dur"]),2))+ '\n'+ "Sum of individual variablels (must be the same as 'Duration Programm'): " +  str(round((options["timestamp_yolo_dur"]+options["timestamp_write_outline_dur"]+options["timestamp_DCE_dur"]+options["timestamp_write_video_dur"]),2)) + "sec." + '\n' + "Minimal deviations due to not exact timestamp setting"
        

    f.write(str(results))
    print("timestamps saved")
    f.close()
    return 0




def save_timestamps_as_file(options):
    f = open( options["path_write_timestamps"], 'w' )
    options["timestamp_prog_end"] = time.time()
    results = "Duration Program: " +ret_timestampline(options, "prog")+ '\n' +"Duration YOLO: " +ret_timestampline(options, "yolo")+ '\n'+"Duration write_Outline(include DCE Calculation) "+str(round((options["timestamp_write_outline_end"]-options["timestamp_write_outline_start"]),2))+" ms" + '\n'+"Duration DCE: " +str(round(options["timestamp_DCE_dur"],2))+" ms" + '\n'+ "Duration write_video: """ +ret_timestampline(options, "write_video") + '\n'+ "Sum of individual variablels (must be the same as 'Duration Programm'): " +  str(round((options["timestamp_yolo_end"]-options["timestamp_yolo_start"])+(options["timestamp_write_outline_end"]-options["timestamp_write_outline_start"]-options["timestamp_DCE_dur"])+options["timestamp_DCE_dur"]+(options["timestamp_write_video_end"]-options["timestamp_write_video_start"]),2)) + "sec." + '\n' + "Minimal deviations due to not exact timestamp setting"
        

    f.write(str(results))
    print("timestamps saved")
    f.close()
    return 0

def ret_timestampline(options, string):
    time_in_ms = round((options["timestamp_"+string+"_end"]-options["timestamp_"+string+"_start"]) * 100, 2)
    time_in_s = round((time_in_ms /100), 2)
    time_in_min = round((time_in_s/60),2)
    if (time_in_s > 180):
        return str(time_in_ms) +" ms / "+str(time_in_s)+" sec /" + str(time_in_min)+" min," 
    else:
        return str(time_in_ms) +" ms / "+str(time_in_s)+" sec," 
   
    
    
main()