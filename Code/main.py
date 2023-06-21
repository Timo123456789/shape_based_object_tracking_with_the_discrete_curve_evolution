from YOLO.yolo_result_version import *
from YOLO.yolo_every_frame import *
#from DCE.DCE import * 


def main():
    #path_source_video = r'Code\vid_examples\left_Side\not_stabilized\autobahn_6.mp4'
    #path_source_video = r'Code\vid_examples\right_Side\autobahn1s.mp4'
   # path_write_video = r'Code\YOLO\runs\videos_from_frames\autobahn_xy_temp.mp4'
    options = {
            #"path_source_video": r'Code\vid_examples\left_Side\not_stabilized\autobahn_6.mp4',
            "path_source_video": r'Code\vid_examples\right_Side\autobahn_2.mp4',
            "path_write_video": r'Code\YOLO\runs\videos_from_frames\autobahn1s_result_version_long.mp4',

        	"NoP_Cars": 10, #Number of final Points for Cars, first try: 10, second try: 25
        	"NoP_Motorcycle": 5, #Number of final Points for Motorcycles, first try: 5, second try: 20
        	"NoP_Truck": 8, #Number of final Points for Trucks, first try: 8, second try:45
        	"NoP_other_Object": 20, #Number of final Points for other Objects, first try: 20, second try:60

            "black_video": True,
            "write_labels": True,
            "calc_K_with_Dist": False,
            "yolo_every_frame": False

    }
    #run_yolo_result_version(options)
    if (options["yolo_every_frame"] == True):
        run_yolo_every_frame_version(options)
    else:
        run_yolo_result_version(options)

   
def run_yolo_every_frame_version(options):
    run_yolo_every_frame_version_intern(options)
    return 0



def run_yolo_result_version(options):
    model = YOLO('yolov8n-seg.pt') 
    results = model.predict(options["path_source_video"], save=False)

    res_outline = get_outline_for_every_object(results, options)

    write_video(res_outline, options["path_write_video"], options["path_source_video"])
    return 0

main()