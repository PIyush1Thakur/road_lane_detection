# 🚗 Road Lane Detection using OpenCV

A simple real-time lane detection system built using classical computer vision techniques in OpenCV. The project detects lane markings from a video and overlays them on the road in real time.

---



## 🧠 How It Works

The pipeline follows these steps:

1. Resize input frame for consistency  
2. Convert frame to grayscale  
3. Apply Gaussian blur to reduce noise  
4. Detect edges using Canny edge detector  
5. Apply Region of Interest (ROI) mask  
6. Detect line segments using Hough Transform  
7. Separate left and right lanes using slope  
8. Average lines to form stable lane boundaries  
9. Overlay detected lanes on original frame  

---

## 🛠️ Tech Stack

- Python
- OpenCV
- NumPy

---

## 📂 Project Structure
road_lane_detection/ <br>
│   <br>
├── road_lane_detection.py  <br>
└── requirements.txt <br>

---

## ⚙️ Installation

### Clone and run the project

```bash
git clone https://github.com/PIyush1Thakur/road_lane_detection.git
cd road_lane_detection
pip install -r requirements.txt
python3 road_lane_detection.py
```
---




https://github.com/user-attachments/assets/a7e21865-a1d6-42d0-a524-b5fd7751ed02


---


