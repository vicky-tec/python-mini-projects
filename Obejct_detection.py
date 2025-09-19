import cv2
import torch
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  

# Open webcam
video_cap = cv2.VideoCapture(0)

while True:
    ret, frame = video_cap.read()
    # Check if frame is captured successfully
    if not ret:
        print("Failed to capture video")
        break

    # Run YOLOv8 object detection
    results = model(frame)

    # Draw bounding boxes
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get box coordinates
            label = result.names[int(box.cls[0])]  # Get object label
            conf = box.conf[0]  # Confidence score

            # Draw rectangle and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cv2.putText(frame, f"{label} ({conf:.2f})", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
            cv2.putText(frame, f"Class: {label}", (x1, y1 - 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
            
    # Resize frame for better display
    frame = cv2.resize(frame, (640, 480))
    # Show the frame with detections
    cv2.imshow("YOLOv8 Object Detection", frame)

    # Display the video feed with detected objects
    cv2.imshow("Object Detection", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

# Release resources
video_cap.release()
cv2.destroyAllWindows()
