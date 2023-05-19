#codesource: https://towardsdatascience.com/enhanced-object-detection-how-to-effectively-implement-yolov8-afd1bf6132ae



from ultralytics import YOLO

# 8n = sehr schnell, aber ungenau, 8m = schnell recht genau, 8x = langsam aber sehr genau
model = YOLO('yolov8n.pt')
results = model(r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\vid_examples\right_Side\autobahn_2.mp4', save=True)

#