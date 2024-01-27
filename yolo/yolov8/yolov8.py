from ultralytics import YOLO
model = YOLO('yolov8n.pt')

resumts= model.track(source='0',show=True,save=True)