from YOLO.yolo_result_version import *
from DCE.DCE import * 


def main():
    path_source_video = r'Code\vid_examples\right_Side\autobahn_2.mp4'
    path_write_video = r'Code\YOLO\runs\videos_from_frames\video_results_main.mp4'

    NoP_Cars = 10
    NoP_Motorcycle = 15
    NoP_Truck = 20

    model = YOLO('yolov8n-seg.pt') 
    results = model.predict(path_source_video, save=False)
    p = choosePolygon(2)
    plot_GS_polygon(simplify_polygon(p, 4))
    # testimg = results[10].plot()
    # cv2.imshow("result", testimg)       
    # cv2.waitKey(0)
    res_outline = get_outline_for_every_object(results, NoP_Cars, NoP_Motorcycle, NoP_Truck)

    write_video(res_outline, path_write_video, path_source_video)
    return 0


main()