from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')
results = model(r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\yolov8_segmentation-pysource.com_\yolov8_segmentation-pysource.com\autobahn1s.mp4', save=True)
print(results[3].masks)