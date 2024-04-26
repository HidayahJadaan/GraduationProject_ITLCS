# Graduation Project - ITLCS

## Description of the Idea
Current traffic lights do not have feedback mechanisms; they only change signals based on a fixed time principle. Such a
system causes many previously mentioned problems. In this project, the feedback signal is entered into the traffic light
processing system (i.e. the Nvidia Jetson Nano) by adding a camera on each road and using those cameras to count the
number of vehicles per road using object detection techniques.
ITLCS uses a webcam to capture the video stream of each road in the intersection such that our traffic light processing
the system receives feedback.
The system is a combined hardware-software structure. The hardware part consists of the Nvidia Jetson Nano
microcomputer and four cameras. The software part was written using Python scripting language and OpenCV which is an
open-source image processing and machine learning library. The system takes the video stream of each road from the web
cameras at traffic junctions and then sends them to the Nvidia Jetson Nano microcomputer. Then the Jetson Nano analyzes the
video stream received from all roads frame-by-frame simultaneously using tools available in the OpenCV library. Then it
detects the road with the largest number of vehicles and provides appropriate time to adjust the traffic flow in each road of
the intersection so that the road with the highest vehicle density has a longer open time slot than other roads.
Also, it maintains the total intersection time ratio, so the road with lower density gets an open time slot without waiting
forever. The estimated time for each road will be based on the number of vehicles according to this equation:


### T = N × A
Where T is the turn-on time, N is the number of cars and A is the average time that cars need to pass the traffic light.
If the estimated time is greater than a predefined maximum road allowed time T (estimated) > T(max), the available
time will equal T(max). Also, if the estimated time is less than a predefined minimum road allowed time T (estimated) <
T(min), the available time will equal T(min).
The selection of the minimum and maximum green phase durations depends on the study area's traffic characteristics and
the space available for vehicles to queue. A minimum limit on the green phase duration usually is required for safety and to
guarantee that no phase is skipped. A maximum limit on the green phase duration is generally defined to limit the green
extension to just one road.


# System Architecture and Design
## Hardware System Components:
The ITLCS consisted of multiple hardware components:
1. NVIDIA Jetson Nano
2. USB Webcams
3. LED Traffic Lights

![Screenshot (264)](https://github.com/HidayahJadaan/GraduationProject_ITLCS/assets/121747756/af4043b8-0d1b-4758-bfa8-5cf9e8750796)

The RED and YELLOW LEDs are directly connected to the GPIO pins and into the ground. While the GREEN LED
is connected to the BJT-PNP Transistor and into the ground. The BJT-PNP Transistor amplifies the current to meet the
requirements of the GREEN LED. This ensures that the GREEN LED receives enough current to emit light at its intended
brightness. The Electrical connection of the LEDs is described in Figure 2.

![Screenshot (265)](https://github.com/HidayahJadaan/GraduationProject_ITLCS/assets/121747756/828a4da8-4189-4017-816a-da516c8e9fe4)
The camera is installed at a suitable height and angle, as shown in Figure 3, that will result in better coverage. 
Better coverage will result in higher accuracy for detection. The coordinates and angle at which the camera is installed are
obtained by experiments to ensure the best possible coverage. The camera is placed on the floor instead of on top of the
traffic light due to its size. In a real-world scenario, the camera would be placed on top of the traffic light.
![Screenshot (266)](https://github.com/HidayahJadaan/GraduationProject_ITLCS/assets/121747756/4ba5495a-f685-4048-9185-059983e5b5e8)

## Software used to interface these hardware components:
The software code was structured into 5 modules:
1. Pre-Trained YOLOv4 DNN model:
   The DNN model learns to recognize patterns and features that are relevant to the vehicles.
The model adjusts its internal parameters (weights and biases) to optimize its performance on the training data. This training
process requires computational power and a long time to improve the accuracy of detection. The weights and configurations
were stored successfully to avoid any loss, by connecting Google Cloab with Google Drive.
Using a pre-trained model saves both time and resources (Saboora et al. 2020) without the need to train a DNN model
from scratch. So as with many modern engineering solutions, a pre-trained DNN model was fine-tuned on a smaller dataset
to be compatible with the ITLCS demo.

3. Vehicle_detector module:
   This module processes the input images and detects vehicles within them. It utilizes image processing algorithms to
analyze the images and identify vehicles' positions. The output of this module is an array where each element of it
represents the detected vehicles’ coordinates which is the position of a detected vehicle. The position is defined by the
coordinates of the top-left point coordinates (x, y) and the width (w) and height (h) of the bounding box surrounding the
vehicle.
4. Vehicle_counting module:
   This module takes the detected vehicle's coordinates as input and performs vehicle counting. It knows the total
number of vehicles, by counting the elements in the array. Additionally, it draws rectangles on each vehicle for visual
verification of the model's accuracy.

5. Run_lights module:
   This module is responsible for controlling the GPIO pins to physically operate the traffic lights. It receives
instructions based on the sorted list of vehicles and their associated traffic lights then activates the appropriate signals.

6. Main module.

![Screenshot (267)](https://github.com/HidayahJadaan/GraduationProject_ITLCS/assets/121747756/c32d801a-5f14-4a87-9d82-8a59a8e1ebeb)

![Screenshot (268)](https://github.com/HidayahJadaan/GraduationProject_ITLCS/assets/121747756/17dd7868-2836-42f4-8c47-1d1cdfc526e7)

