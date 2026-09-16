# 🎥 AI-Based Smart Surveillance & Object Tracking System

<p align="center">
  <b>A modular Computer Vision system for intelligent video surveillance</b>
  <br>
  Detect • Track • Analyze • Log
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white" alt="Python 3.11">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/YOLO-Object%20Detection-purple" alt="YOLO">
  <img src="https://img.shields.io/badge/Project-Computer%20Vision-orange" alt="Computer Vision">
</p>

---

## 📌 Overview

The **AI-Based Smart Surveillance & Object Tracking System** is a Python-based Computer Vision project that processes video footage to detect and track objects, identify motion, and record surveillance events.

The system combines YOLO-based object detection, persistent object tracking, motion analysis, and CSV-based event logging in a modular pipeline.

## ✨ Features

| Feature                 | Description                                    |
| ----------------------- | ---------------------------------------------- |
| 🎞️ Video Input         | Reads and processes video frames               |
| 🖼️ Image Preprocessing | Resizing, denoising, and contrast enhancement  |
| 🎯 Object Detection     | Detects objects using YOLO                     |
| 🧭 Object Tracking      | Tracks detected objects using persistent IDs   |
| 🏃 Motion Detection     | Identifies changes between consecutive frames  |
| 📝 Event Logging        | Stores detected events in CSV format           |
| 📊 Analytics            | Summarizes event counts and object information |
| 🎬 Video Output         | Generates an annotated surveillance video      |

## 🏗️ System Architecture

```text
          ┌──────────────────┐
          │    Input Video   │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │ Video Reader     │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │ Preprocessing    │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │ Object Detection │
          │    & Tracking    │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │ Motion Detection │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │   Event Logger   │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │ Analytics &      │
          │ Annotated Output │
          └──────────────────┘
```

## 🛠️ Tech Stack

* **Language:** Python 3.11
* **Computer Vision:** OpenCV
* **Object Detection & Tracking:** Ultralytics YOLO
* **Data Logging:** CSV
* **Testing:** Python test modules
* **Version Control:** Git & GitHub

## 📂 Project Structure

```text
smart-surveillance-cv/
│
├── analytics/          # Event analytics
├── config/             # Configuration settings
├── detection/          # Object detection module
├── input/              # Input video and video reader
├── logging_module/     # CSV event logging
├── motion/             # Motion detection
├── preprocessing/      # Image preprocessing
├── tracking/           # Object tracking
├── tests/              # Module and pipeline tests
│
├── main.py             # Main application
├── requirements.txt    # Python dependencies
├── yolo11n.pt          # YOLO model weights
├── README.md
└── .gitignore
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/adityasaini2005/smart-surveillance-cv.git
cd smart-surveillance-cv
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## ▶️ Run the Project

Make sure the configured input video and YOLO model are available.

```bash
python main.py
```

The application processes the configured video and generates an annotated output video and a CSV event log.

## 🧪 Testing

Run the tests from the project root:

```bash
python -m tests.test_preprocessing
python -m tests.test_video_reader
python -m tests.test_detection
python -m tests.test_tracking
python -m tests.test_motion
python -m tests.test_logger
python -m tests.test_analytics
python -m tests.test_pipeline
python -m tests.test_system
```

## 📈 Sample Execution Results

The system was tested on the configured input video.

| Metric                      | Result |
| --------------------------- | -----: |
| Frames processed            |    186 |
| Logged events               |  1,245 |
| Distinct tracker IDs in log |     23 |
| Average logged confidence   |   0.69 |

**Detected object categories included:**

* Person
* Traffic light
* Car
* Motorcycle
* Bicycle

> Note: Logged events can include repeated observations of the same tracked object across multiple frames. Tracker IDs do not necessarily represent unique real-world individuals.

## 📁 Output Files

Generated files are saved in the `output/` directory:

| File                      | Purpose                      |
| ------------------------- | ---------------------------- |
| `surveillance_output.mp4` | Annotated processed video    |
| `events.csv`              | Recorded surveillance events |

## 🎯 Project Objectives

* Apply Computer Vision concepts to a practical surveillance scenario.
* Integrate object detection and tracking into a modular application.
* Analyze motion between consecutive frames.
* Record events and generate useful summaries.
* Practice software design, testing, and version control.

## 🚀 Future Improvements

* Reduce duplicate event logging.
* Add configurable detection and motion thresholds.
* Develop a dashboard for event visualization.
* Support live camera input.
* Evaluate performance under different lighting and motion conditions.

## 👨‍💻 Author

**Aditya Saini**

B.Tech — Computer Science & Engineering (AI & ML)
VIT Bhopal University

## 🔗 Repository

[View the project on GitHub](https://github.com/adityasaini2005/smart-surveillance-cv)

---

<p align="center">
  <i>Built as a Computer Vision project for learning and experimentation.</i>
</p>
