from ultralytics import YOLO
import numpy as np




class YOLOSegmentation:
    """
    class object to contains all functions

    Source: https://pysource.com/2023/02/21/yolo-v8-segmentation
    """
    def __init__(self, model_path):
        """
        init YOLO modell

        @param self: class itself
        @param modelpath: path where YOLO Modell is located

        Source: https://pysource.com/2023/02/21/yolo-v8-segmentation
        """
        self.model = YOLO(model_path)

    def detect(self, img):
        """
        detect objects on a given img and returns detected values as array

        @param self: class itself
        @param img: image, which would be analzyed with YOLO
        @return:  bboxes, class_ids, segmentation_contours_idx, scores as array

        Source: https://pysource.com/2023/02/21/yolo-v8-segmentation
        """
        # Get img shape

        height, width, channels = img.shape

        results = self.model.predict(source=img.copy(), save=False, save_txt=False)
        result = results[0]
        segmentation_contours_idx = []
    

        bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
        # Get class ids
        class_ids = np.array(result.boxes.cls.cpu(), dtype="int")
        # Get scores
        scores = np.array(result.boxes.conf.cpu(), dtype="float").round(2)
        
        segmentation_contours_idx = result.masks.xy
        return bboxes, class_ids, segmentation_contours_idx,  scores


