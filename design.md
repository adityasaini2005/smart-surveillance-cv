

\# System Architecture and Design



\## 1. Project Title

AI-Based Smart Surveillance and Object Tracking System



\## 2. System Overview

The system processes a surveillance video using Python,

OpenCV, and YOLO. It detects and tracks objects, identifies

motion between frames, records object information, and

generates a processed video with basic analytics.



\## 3. System Architecture



```mermaid

flowchart TD

&#x20;   A\[Input Video] --> B\[Video Reader]

&#x20;   B --> C\[Image Preprocessing]

&#x20;   C --> D\[YOLO Object Detection and Tracking]

&#x20;   C --> E\[Motion Detection]

&#x20;   D --> F\[Draw Tracking Results]

&#x20;   E --> G{Motion Detected?}

&#x20;   G -->|Yes| H\[Event Logger]

&#x20;   G -->|No| I\[Continue Processing]

&#x20;   H --> I

&#x20;   I --> F

&#x20;   F --> J\[Output Video]

&#x20;   H --> K\[CSV Event Log]

&#x20;   K --> L\[Analytics]

&#x20;   L --> M\[Event Statistics]

```



\## 4. Process Flow



1\. The user provides a video file.

2\. The video reader opens the file and reads its frames.

3\. Each frame is resized and preprocessed.

4\. YOLO detects and tracks objects in the frames.

5\. The motion detection module compares consecutive frames.

6\. If motion is detected, information about tracked objects

&#x20;  is recorded in the CSV event log.

7\. Detection and tracking information is drawn on the frames.

8\. The processed frames are combined into an output video.

9\. Analytics are calculated from the recorded event log.



\## 5. Module Description



\### 5.1 Input Module

File: `input/video\_reader.py`



Reads the input video, checks whether it can be opened,

and provides frames for processing.



\### 5.2 Preprocessing Module

File: `preprocessing/image\_processor.py`



Resizes frames, converts images to grayscale, applies

Gaussian denoising, and performs contrast enhancement.



\### 5.3 Object Detection Module

File: `detection/object\_detector.py`



Uses the YOLO model to identify objects and obtain their

class names, confidence values, and bounding boxes.



\### 5.4 Object Tracking Module

File: `tracking/object\_tracker.py`



Uses YOLO tracking to follow detected objects across

consecutive frames and obtain tracking IDs.



\### 5.5 Motion Detection Module

File: `motion/motion\_detector.py`



Compares consecutive frames to identify changes that

may indicate motion.



\### 5.6 Event Logging Module

File: `logging\_module/event\_logger.py`



Stores information about tracked objects during detected

motion in a CSV file.



\### 5.7 Analytics Module

File: `analytics/analytics.py`



Reads the CSV event log and calculates the total number

of recorded events, unique object IDs, object types,

and average confidence.



\### 5.8 Configuration Module

File: `config/config.py`



Stores the input video path, output paths, model path,

frame width, and motion detection thresholds.



\### 5.9 Main Module

File: `main.py`



Connects the modules and controls the complete

video processing workflow.



\## 6. Data Flow



The input video is converted into individual frames.

These frames are preprocessed and passed through the

object tracking and motion detection stages.



The tracking results are used to draw object information

on the output frames. When motion is detected, tracked

object information is sent to the event logger.



The logger saves the records in a CSV file. The analytics

module reads this file and calculates summary statistics.



\## 7. Software Design



The project follows a modular design. Each module handles

a specific task, such as reading videos, preprocessing

images, tracking objects, or recording events.



The main program connects these modules. This structure

makes it easier to test individual components and modify

the system in the future.



\## 8. Current Limitations



\- The current system processes video files rather than

&#x20; live CCTV streams.

\- Motion detection is based on frame differences.

\- The event log can contain repeated observations of

&#x20; the same tracked object.

\- The system does not classify activities as suspicious.



\## 9. Future Improvements



\- Support live camera input.

\- Reduce repeated event records.

\- Add alerts for selected events.

\- Improve motion and activity analysis.

