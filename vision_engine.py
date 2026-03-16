import cv2
from ultralytics import YOLO
import pandas as pd

# Load the AI Model
model = YOLO('yolov8n.pt') 

# Video source: Use 0 for Webcam, or 'video.mp4' for a file
cap = cv2.VideoCapture(0) 

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Run YOLOv8 detection (only for class 0: Person)
    results = model(frame, classes=0, conf=0.4, verbose=False)
    
    # Get total count
    passenger_count = len(results[0].boxes)

    # Save count to a CSV file (The "Bridge")
    df = pd.DataFrame({'count': [passenger_count]})
    df.to_csv('live_data.csv', index=False)

    # Display the AI view (Optional)
    annotated_frame = results[0].plot()
    cv2.putText(annotated_frame, f"Count: {passenger_count}", (50, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("MetroEye Vision Engine", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()