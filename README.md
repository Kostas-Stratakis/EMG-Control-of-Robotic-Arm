# EMG-Control-of-Robotic-Arm
This project 's goal is to control a robotic arm built from lego using EMG signal recorded from a user performing static gestures.
The main idea is that, the user performs  a number static gestures 10 seconds each and records the signal.
These signals are stored to create data-sets. These data-sets are used train an SVM that does the recognition (classification) of each gesture.
After the classification a corresponding  command to start or stop a motor is sent to the Lego NXT, which is the microprocessor that controls the motors.

In this repository, except the Readme and the License files, there are 6 other files. A short description for each one of them follows:
Signal amplifiers.png: This schematic depicts the analog circuit needed to be built for recording the EMG signal from a pair of muscles of interest.
Power supply circuit.png: The schematic for powering up the aforementioned circuit.
Microprocessor Software: The code running on an STM32 Nucleo board. It samples the signal filters it and then Rms values over a window are sent to a PC.
Finding_best_SVM_for_5gestures.py: This python code uses scikit-learn library to train SVMs with different parameters to find the best among them that classifies the gestures correctly. The data-sets needed for the trainig are created by storing the values sent by Microprocessor Software.
Sending_real-time_Commands.py: This python code takes the parameters found from the previous python code and trains and SVM. This SVM receives data (vectors) in real-time and classifies it trying to recognize the gesture the user is doing. Based on the gesture recognized commands are sent via bluetooth  to the NXT fro motor control.
Myoelectric Control of Robotic Arm Msc Thesis.pdf: This document is my diploma thesis. All the details and the knowledge needed for understanding and building this project are included. In the conclusion chapter the inherent dificulties and and the aspects that need more researching are stated and explained.

A video showing real-time operation classifying among 5 gestures and recording from 4 muscles of interest exist in the follwing google drive link:

https://drive.google.com/open?id=1bZBQOkEBfMYjs1B4Ci36rJVv6ELplE3P
