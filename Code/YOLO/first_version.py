#codesource: https://towardsdatascience.com/enhanced-object-detection-how-to-effectively-implement-yolov8-afd1bf6132ae

from ultralytics import YOLO
import numpy as np




def main(): 
    path = r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\vid_examples\right_Side\autobahn_2.mp4'
    # 8n = sehr schnell, aber ungenau, 8m = schnell recht genau, 8x = langsam aber sehr genau
    # results = analyse_vid(path)
    # write_results_file(results)
    results = read_results_file()
    print("________________________________________________________________________________________________________________")
    print("________________________________________________________________________________________________________________")
    #print(raw_results[0].masks)
    print("________________________________________________________________________________________________________________")
    results_without_arr = results[0]
    print(results_without_arr.masks)
    
  

def read_results_file():
    f = open(r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\YOLO\temp\results.py')
    contents = f.read()
    return (contents)

def write_results_file(results):
    f = open( r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\YOLO\temp\results.py', 'w' )
    f.write(repr(results))
    f.close()

def analyse_vid(path):
    model = YOLO('yolov8n-seg.pt')
    results = model(path, save=True)
    return results



main()