# To run smoothly on your local machine instead of the cloud:
import cv2
from ultralytics import YOLO

model = YOLO("best.pt")
model.predict(source="0", show=True)