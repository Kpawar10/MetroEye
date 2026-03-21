🚉 MetroEye: AI-Based Crowd Monitoring System
📌 Overview

MetroEye is a real-time crowd monitoring system that uses computer vision to estimate passenger occupancy in metro environments. It leverages deep learning-based head detection to handle dense crowd scenarios and provides live insights through an interactive dashboard.


🚀 Key Features

🎯 Real-time passenger counting from video streams

🧠 Head detection using YOLOv8 for dense crowd handling

📊 Interactive dashboard for live monitoring

🌡️ Heatmap-based crowd density visualization

📈 Time-series analysis for peak hour detection

⚡ Optimized detection performance under occlusion


🧠 Problem Statement

Accurate crowd estimation in metro systems is challenging due to:

High density and occlusion

Overlapping individuals

Lack of real-time analytics systems

MetroEye solves this by using head detection instead of full-body detection, improving accuracy in crowded environments.

🏗️ System Architecture
Video Input (CCTV / File)
        ↓
Frame Extraction (OpenCV)
        ↓
Head Detection (YOLOv8)
        ↓
Passenger Counting Logic
        ↓
Data Logging
        ↓
Streamlit Dashboard (Visualization)
⚙️ Tech Stack

Python

YOLOv8 (Ultralytics)

OpenCV

Streamlit

Pandas, NumPy

Matplotlib / Seaborn

📊 Model Performance
Metric	Value
Precision	81%
Recall	50%
mAP@0.5	64%
📌 Insights

High precision reduces false positives (avoiding overcounting)

Lower recall due to occlusion and small object sizes in dense crowds

📈 Dashboard Preview

(Add screenshots here after deployment)

Live passenger count

Crowd density classification (Low / Medium / High)

Heatmap visualization

Peak hour trends
