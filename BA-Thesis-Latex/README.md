# Formbasiertes Objekttracking mit der Discrete Curve Evolution
# Shape-based object tracking with the Discrete Curve Evolution

## Bachelor Thesis an der Westfälischen Wilhelms-Universität Münster, 2023

In dieser Arbeit wird ein Ansatz zu formbasiertem Objekttracking mit der Discrete Curve Evolution (DCE) vorgestellt. Zur Detektion der Objekte wird maschinelles Lernen namens YOLO verwendet und das Ergebnis des Objekttrackings wird mit einem Formähnlichkeitsmaß für jedes Polygon bewertet. Es wird eine prototypische Implementierung beschrieben, die auf der Programmiersprache Python basiert. Die Evaluation des Ansatzes erfolgt an mehreren Testvideos für den Anwendungsfall Verkehrstracking mit verschiedenen YOLO-Modellen. Im Rahmen dieser Arbeit zeigt sich, dass detektierte Objekte und deren vereinfachte Umrisse geringe Abweichungen aufweisen. Diese Abweichungen bleiben auch bei Eingabedaten, die nicht dem ursprünglichen Anwendungsfall entsprechen, gering, sodass der Ansatz nicht nur auf Verkehrstracking beschränkt ist. Da diese Abweichungen außerdem gleichbleibend gering über den gesamten Verlauf eines Videos bleiben, ist ein formbasiertes Objekttracking mit der Discrete Curve Evolution möglich.

### Timo Lietmeyer, 28.09.2023