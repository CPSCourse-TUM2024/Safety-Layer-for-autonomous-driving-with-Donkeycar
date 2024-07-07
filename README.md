# Safety-Layer-for-autonomous-driving-with-Donkeycar
This project was created for the Embedded Systems, Cyber-Physical Systems and Robotics course.\
This project aims to introduce a safety layer on top of a common reinforcement learning library.\
We are using a Jetracer car, the purpose of which is to learn, develop, and test machine learning models for autonomous driving.\
We developed an RNN model that performs the basic function of driving and turning with some basic collision detection.\
It has proven inadequate to secure the complete safety of driving without hitting objects.\
Therefore, we have decided to develop a safety layer on top of the Donkeycar library to prevent collisions and recover from such situations.\
As a base for our idea, we used our course Professor Amr Alanwar's collaborative research project https://github.com/Mahmoud-Selim/Safe-Reinforcement-Learning-for-Black-Box-Systems-Using-Reachability-Analysis

## Hardware Platform
Our project uses the following platform to develop and run our implementation.\
https://www.waveshare.com/product/jetracer-ros-ai-kit.htm \
It is a JetRacer ROS kit from waveshare.\
Components: Raspberry Pi RP2040 Chip, 37-520 Metal Encoder Motor, 11 wire AB phase hall speed sensor, supports wheel odometry, IMU sensor MPU9250, Lidar RPLIDAR A1

## Donkey library
### Setup
### Model Selection
### Model Training
## Track
## Safety Layer
### Virtual Track
### Updating virtual location
### Computing collision
### Recovery
## Connecting Donkey with Safety layer
## Results
## Conclusion
