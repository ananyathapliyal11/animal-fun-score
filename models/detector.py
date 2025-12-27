from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_animals(image_path):
    image = cv2.imread(image_path)
    results = model(image)[0]
    animals = []
    for box in results.boxes:
        cls = int(box.cls[0])
        label = results.names[cls]

        if label not in ["dog", "cat", "horse", "cow", "sheep", "bird"]:
            continue
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        animals.append({
            "label": label,
            "bbox": (x1, y1, x2, y2),
            "confidence": float(box.conf[0])
        })
    return image, animals
