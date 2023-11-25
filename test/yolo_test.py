from ultralytics import YOLO
import cv2

# モデル読み込み
model = YOLO("yolov8n.pt")
results = model('img/face.jpg', save=True)
