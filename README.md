\# AI-Based Smart Surveillance \& Object Tracking System



\## Overview



A Computer Vision project that analyzes video footage to detect and track objects, identify motion, and log surveillance events.



\## Features



\* Video input and frame processing

\* Object detection using YOLO

\* Object tracking with persistent IDs

\* Motion detection between frames

\* Event logging in CSV format

\* Analytics on detected events

\* Annotated surveillance video output



\## Technologies Used



\* Python 3.11

\* OpenCV

\* Ultralytics YOLO

\* CSV



\## Project Structure



\* `main.py` – Main surveillance pipeline

\* `input/` – Input video and video reader

\* `preprocessing/` – Image preprocessing

\* `detection/` – Object detection

\* `tracking/` – Object tracking

\* `motion/` – Motion detection

\* `logging\_module/` – Event logging

\* `analytics/` – Event analytics

\* `config/` – Configuration settings

\* `tests/` – Module tests



\## Installation



1\. Clone the repository:



&#x20;  ```bash

&#x20;  git clone https://github.com/adityasaini2005/smart-surveillance-cv.git

&#x20;  cd smart-surveillance-cv

&#x20;  ```



2\. Install dependencies:



&#x20;  ```bash

&#x20;  pip install -r requirements.txt

&#x20;  ```



\## Run the Project



```bash

python main.py

```



The configured input video is processed, and the system generates an annotated output video and a CSV event log.



\## Testing



Run individual tests using:



```bash

python -m tests.test\_preprocessing

python -m tests.test\_video\_reader

python -m tests.test\_detection

python -m tests.test\_tracking

python -m tests.test\_motion

python -m tests.test\_logger

python -m tests.test\_analytics

python -m tests.test\_pipeline

python -m tests.test\_system

```



\## Outputs



\* Annotated video: `output/surveillance\_output.mp4`

\* Event log: `output/events.csv`



\## Project Purpose



Develop a modular Computer Vision surveillance system that combines object detection, tracking, motion analysis, and event-based reporting.



