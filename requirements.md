

\# Software Requirements



\## 1. Project Title

AI-Based Smart Surveillance and Object Tracking System



\## 2. Introduction

This project uses computer vision to detect and track objects in a

surveillance video. It also detects motion, records related object

information in a CSV file, and generates a processed video.



\## 3. Functional Requirements



FR-1: The system should read a video file from the input folder.



FR-2: The system should check whether the video can be opened and

read its frames.



FR-3: The system should resize video frames and apply image

preprocessing techniques.



FR-4: The system should detect objects in video frames using YOLO.



FR-5: The system should track detected objects across video frames.



FR-6: The system should detect motion by comparing consecutive

frames.



FR-7: When motion is detected, the system should record information

about tracked objects in a CSV file.



FR-8: The system should generate an output video showing object

detection and tracking results.



FR-9: The system should display basic analytics, including the

number of recorded events, object types, and average confidence.



\## 4. Non-Functional Requirements



NFR-1: The code should be divided into separate modules so that

each part can be maintained independently.



NFR-2: The system should handle an invalid or unavailable video

file without continuing normal processing.



NFR-3: The system should process video frames in sequence.



NFR-4: The output video and event log should be saved in the

specified output folder.



NFR-5: The system should be easy to run using Python and the

required libraries.



NFR-6: Individual modules should be testable separately.



\## 5. Hardware Requirements



\- Computer or laptop

\- Minimum 8 GB RAM recommended

\- CPU; a compatible GPU can be used for faster processing

\- Storage space for input and output videos



\## 6. Software Requirements



\- Windows or another Python-supported operating system

\- Python 3.11

\- OpenCV

\- Ultralytics YOLO

\- NumPy

\- Git and GitHub



\## 7. Input and Output



Input:

\- A video file placed in the input folder.



Output:

\- Processed surveillance video.

\- CSV file containing recorded object events.

\- Basic analytics printed after processing.



\## 8. Limitations



\- The current version processes a video file, not a live CCTV feed.

\- Motion detection is based on differences between video frames.

\- The CSV may contain repeated observations of the same tracked

&#x20; object.

\- The system does not independently determine whether an activity

&#x20; is suspicious.



\## 9. Future Improvements



\- Add live camera support.

\- Reduce repeated event records.

\- Add notifications for selected events.

\- Improve motion and activity analysis.

