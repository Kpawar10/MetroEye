import cv2
from ultralytics import YOLO
import pandas as pd
import numpy as np
from datetime import datetime
import os
import time

# Load YOUR trained model (IMPORTANT)
model = YOLO('C:\\Users\\kriti\\Downloads\\archive\\CrowdHuman\\runs\\detect\\train7\\weights\\best.pt') 

cap = cv2.VideoCapture(0) 

# Initialize heatmap
heatmap = None
last_saved_time = 0 


file_path = 'live_data.csv'

# ✅ Create CSV file with header if not exists
if not os.path.exists(file_path):
    df_init = pd.DataFrame(columns=['time', 'count', 'status'])
    df_init.to_csv(file_path, index=False)  

while cap.isOpened():
    start_time = time.time() 

    success, frame = cap.read()
    if not success:
        break

    # Detection
    results = model(frame, conf=0.15,classes=0)

    # Initialize heatmap
    if heatmap is None:
        heatmap = np.zeros((frame.shape[0], frame.shape[1]), dtype=np.float32)

    # Add heat from detections
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        h, w = heatmap.shape
        if 0 <= cx < w and 0 <= cy < h:
            heatmap[cy, cx] += 1

    # 🔥 Prevent infinite brightness
    heatmap *= 0.95

    # Normalize heatmap
    heatmap_blur = cv2.GaussianBlur(heatmap, (15, 15), 0)
    heatmap_norm = cv2.normalize(heatmap_blur, None, 0, 255, cv2.NORM_MINMAX)
    heatmap_uint8 = heatmap_norm.astype(np.uint8)
    heatmap_color = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_JET)

    # Overlay
    annotated_frame = results[0].plot()   # 🔥 shows bounding boxes
    overlay = cv2.addWeighted(annotated_frame, 0.6, heatmap_color, 0.4, 0)

    # Count
    passenger_count = len(results[0].boxes)

    # ✅ 3-Level Status Logic
    if passenger_count <= 10:
        status = "Low"
        color = (0, 255, 0)
    elif passenger_count <= 25:
        status = "Medium"
        color = (0, 255, 255)
    else:
        status = "High"
        color = (0, 0, 255)

    # Save to CSV
   
    current_timestamp = time.time()
    file_path = 'live_data.csv'
    if current_timestamp - last_saved_time >= 1:  # save every 1 sec
        current_time = datetime.now()
        df = pd.DataFrame({
            'time': [current_time],
            'count': [passenger_count],
            'status': [status]
        })

        df.to_csv(file_path, mode='a', header=False, index=False)

        last_saved_time = current_timestamp

    # Draw text
    cv2.putText(overlay, f"Count: {passenger_count}", (50, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(overlay, f"Status: {status}", (50, 100), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    fps = 1 / (time.time() - start_time)
    cv2.putText(overlay, f"FPS: {int(fps)}", (50, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)


    # Show output
    cv2.imshow("MetroEye Vision Engine (Heatmap)", overlay)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()