import cv2
from yolo_segmentation import YOLOSegmentation

img = cv2.imread(r"Code\vid_examples\kurz.png")
img = cv2.resize(img, None, fx=0.5, fy=0.5)

# Segmentation detector
ys = YOLOSegmentation("yolov8m-seg.pt")

# Segmentation detector
ys = YOLOSegmentation("yolov8m-seg.pt")

bboxes, classes, segmentations, scores = ys.detect(img)
for bbox, class_id, seg, score in zip(bboxes, classes, segmentations, scores):
    # print("bbox:", bbox, "class id:", class_id, "seg:", seg, "score:", score)
    (x, y, x2, y2) = bbox
    if class_id == 2:
        cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), 2)

        cv2.polylines(img, [seg], True, (0, 0, 255), 4)

        cv2.putText(img, str(class_id), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

cv2.imshow("image", img)
cv2.waitKey(0)






























#from google.colab.patches import cv2_imshow


# model = YOLO("yolov8n-seg.pt")
# results = model.predict(r'kurz.png')

# masks = results[0].masks  # Masks object

# H,W,_ = cv2.imread(r'C:\Users\timol\OneDrive - Universität Münster\10. Fachsemester_SS_2023\bachelor-thesis\Code\vid_examples\Screenshot_rS_A2.png').shape

# x = (results[0].masks.segments[0][:,0]*W).astype("int")
# y = (results[0].masks.segments[0][:,1]*H).astype("int")
# blk=np.zeros((H,W))
# blk[y,x] =255
# cv2_imshow(blk.astype("uint8"))