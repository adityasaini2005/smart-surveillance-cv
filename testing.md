

\# Testing and Results



\## 1. Testing



We tested the different modules of our Smart Surveillance

System separately and then ran the complete program using

a sample video.



The tests were performed to check whether the modules

were working correctly and whether the system could

generate the required output.



\## 2. Module Testing



| Module | What We Checked | Result |

|---|---|---|

| Preprocessing | Image resizing and processing | Passed |

| Video Reader | Opening video and reading frames | Passed |

| Object Detection | Detecting objects using YOLO | Passed |

| Object Tracking | Tracking objects across frames | Passed |

| Motion Detection | Detecting changes between frames | Passed |

| Event Logger | Saving event information in CSV | Passed |

| Analytics | Reading CSV and calculating statistics | Passed |

| Pipeline | Connecting the main modules | Passed |



\## 3. Complete System Testing



We ran the main program using the sample video stored in

the input folder. The program processed the video and

generated an output video and event log.



\### Test Results



\- Frames processed: 186

\- Total recorded events: 1245

\- Unique object IDs in the log: 23

\- Average detection confidence: 0.69



\### Detected Object Types



| Object | Recorded Observations |

|---|---:|

| Person | 862 |

| Traffic light | 181 |

| Car | 145 |

| Motorcycle | 6 |

| Bicycle | 51 |



\## 4. Output Files



The program generated the following files:



\- `output/surveillance\_output.mp4`

\- `output/events.csv`



The output video contains the detection and tracking

results. The CSV file stores object information recorded

during detected motion.



\## 5. Observations



The system successfully processed the sample video and

generated the expected output files.



The event log contains repeated observations of objects

across frames. Therefore, the total event count should

not be treated as the number of separate incidents.



The unique object count refers to distinct object IDs

recorded in the CSV file.



\## 6. Conclusion



The tests showed that the implemented modules and the

complete video processing pipeline worked with the

sample video.



The current version demonstrates object detection,

tracking, motion detection, event logging, and basic

analytics. Further improvements can focus on reducing

repeated event records and supporting live camera input.

