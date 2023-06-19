from YOLO.yolo_result_version import *
#from DCE.DCE import * 


def main():
    #path_source_video = r'Code\vid_examples\left_Side\not_stabilized\autobahn_6.mp4'
    path_source_video = r'Code\vid_examples\right_Side\autobahn1s.mp4'
    path_write_video = r'Code\YOLO\runs\videos_from_frames\autobahn_xy_temp.mp4'
    options = {
        	"NoP_Cars": 10, #Number of final Points for Cars, first try: 10, second try: 25
        	"NoP_Motorcycle": 5, #Number of final Points for Motorcycles, first try: 5, second try: 20
        	"NoP_Truck": 8, #Number of final Points for Trucks, first try: 8, second try:45
        	"NoP_other_Object": 20, #Number of final Points for other Objects, first try: 20, second try:60

            "black_video": True,
            "write_labels": True,
            "calc_K_with_Dist": False,
            "yolo_every_frame": False

    }
    

    model = YOLO('yolov8n-seg.pt') 
    results = model.predict(path_source_video, save=False)

    res_outline = get_outline_for_every_object(results, options)

    write_video(res_outline, path_write_video, path_source_video)
    return 0


main()