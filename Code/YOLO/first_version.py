#codesource: https://towardsdatascience.com/enhanced-object-detection-how-to-effectively-implement-yolov8-afd1bf6132ae

from ultralytics import YOLO
import pandas # Source: https://java2blog.com/save-object-to-file-python/
import numpy as np


#masks2segment example : https://stackoverflow.com/questions/75545012/yolov8-segmentation-mask-problem-masks-looks-2-parts-but-outputs-only-first-par



def main(): 
    path = r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\vid_examples\right_Side\autobahn1s.mp4'
    # 8n = sehr schnell, aber ungenau, 8m = schnell recht genau, 8x = langsam aber sehr genau
    results = analyse_vid(path)
    segments = results.masks2segments()
    YOLO.masks
    print(segments)



    
 
 
   


        

def analyse_vid(path):
    model = YOLO('yolov8n-seg.pt')
    results = model(path, save=True)
    return results

def

main()