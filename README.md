🚉 MetroEye: AI-Based Crowd Monitoring System
📌 Overview

MetroEye is a real-time crowd monitoring system designed to estimate passenger occupancy in metro coaches using computer vision. The system leverages deep learning-based object detection to count individuals in dense environments and provides live insights through an interactive dashboard.

🚀 Key Features

Real-time passenger counting from video streams

Head detection in dense crowds using YOLOv8

Live dashboard for monitoring occupancy levels

Heatmap-based crowd density visualization

Time-series analysis for peak hour detection

Model optimization for improved detection performance

🧠 Problem Statement

Accurate crowd estimation in metro systems is challenging due to:

High density and occlusion

Dynamic passenger movement

Lack of real-time monitoring tools

MetroEye addresses these challenges by using head detection instead of full-body detection to improve accuracy in crowded environments.

🏗️ System Architecture

Video input (CCTV / simulated stream)

Frame extraction using OpenCV

Object detection using YOLOv8

Passenger counting logic

Data logging for occupancy tracking

Streamlit dashboard for visualization

⚙️ Tech Stack

Python

YOLOv8 (Ultralytics)

OpenCV

Streamlit

Pandas & Matplotlib

📊 Model Performance

Precision: 81%

Recall: 50%

mAP@0.5: 64%

📌 Insights:

Higher precision ensures fewer false positives (avoiding overcounting)

Lower recall due to occlusion and small object size in dense crowds

📈 Dashboard Features

Live passenger count

Crowd density classification (Low / Medium / High)

Heatmap visualization

Historical trends and peak hour analysis

🔍 Key Learnings

Handling occlusion in dense object detection

Trade-off between precision and recall

Real-time inference optimization

Building end-to-end ML pipelines

⚡ Future Improvements

Integrate object tracking (e.g., DeepSORT) to avoid double counting

Deploy on edge devices for real-time metro integration

Multi-camera support for full station coverage

Alert system for overcrowding detection

▶️ How to Run
1. Clone the repository
git clone https://github.com/your-username/metroeye.git
cd metroeye
2. Install dependencies
pip install -r requirements.txt
3. Run the Streamlit app
streamlit run app.py
📁 Project Structure
MetroEye/
│── app.py
│── model/
│   └── yolov8_weights.pt
│── data/
│── utils/
│── notebooks/
│── requirements.txt
│── README.md
🎯 Use Cases

Smart metro systems

Railway station crowd monitoring

Event crowd management

Public safety analytics

🧑‍💻 Author

Kritika Pawar
Aspiring Data Scientist
