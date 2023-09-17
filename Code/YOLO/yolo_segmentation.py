"""
YOLO Result Version Code File for a prototypical implementation for the combination of "You Only Look Once" (YOLO) (Redmon, 2016, doi: 10.1109/CVPR.2016.91 ) (Vers. YOLOv8x, Ultralytics, 2023) and Discrete Curce Evolution (DCE) (Latecki, 1999, doi: 10.1006/cviu.1998.0738 ); based on hypothesis by Dorr, Latecki and  Moratz (2015, doi: 10.1007/978-3-319-23374-1_7 )

Runs the YOLO AI Model in form of run YOLO for the whole video and calculate DCE after this for all detected polygons

Must be used with the files: Main.py, DCE.py,  yolo_every_frame.py, yolo_every_result.py, shape_sim_meas.py

Implementation for bachelor thesis: "Formbasiertes Objekttracking mit der Discrete Curve Evolution"
                                    "Shape-based object tracking with the Discrete Curve Evolution"

                                    at Westfaelische Wilhelms Universitaet Muenster
                                    First Supervisor: Prof. Dr. Ing. Reinhard Moratz
                                    Second Supervisor: Dr. Christian Knoth

@author: Timo Lietmeyer, 11.09.2023
@contact: timolietmeyer@uni-muenster.de (for question, etc.)

supported by Vocavit GmbH, Hamburg

Inspired by Sergej Canu
Source Code: https://pysource.com/2023/02/21/yolo-v8-segmentation

"""

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
        if results is not None and result is not None: #if clause when yolo detected no object
            segmentation_contours_idx = []
        
            bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
            # Get class ids
            class_ids = np.array(result.boxes.cls.cpu(), dtype="int")
            # Get scores
            scores = np.array(result.boxes.conf.cpu(), dtype="float").round(2)
            
            segmentation_contours_idx = result.masks.xy
        return bboxes, class_ids, segmentation_contours_idx,  scores