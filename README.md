# Safety-Layer-for-autonomous-driving-with-Donkeycar
This project was created for the Embedded Systems, Cyber-Physical Systems and Robotics course.\
This project aims to introduce a safety layer on top of a common reinforcement learning library.\
We are using a Jetracer car, the purpose of which is to learn, develop, and test machine learning models for autonomous driving.\
We developed an RNN model that performs the basic function of driving and turning with some basic collision detection.\
It has proven inadequate to secure the complete safety of driving without hitting objects.\
Therefore, we have decided to develop a safety layer on top of the Donkeycar library to prevent collisions and recover from such situations.\
As a base for our idea, we used our course Professor Amr Alanwar's collaborative research project https://github.com/Mahmoud-Selim/Safe-Reinforcement-Learning-for-Black-Box-Systems-Using-Reachability-Analysis \
Paper used: https://doi.org/10.1109/LRA.2022.3192205

## Hardware Platform
Our project uses the following platform to develop and run our implementation.\
https://www.waveshare.com/product/jetracer-ros-ai-kit.htm \
It is a JetRacer ROS kit from waveshare.\
Components: Raspberry Pi RP2040 Chip, 37-520 Metal Encoder Motor, 11 wire AB phase hall speed sensor, supports wheel odometry, IMU sensor MPU9250, Lidar RPLIDAR A1\

## Track
![IMG_1552](https://github.com/ValachPatrik/Safety-Layer-for-autonomous-driving-with-Donkeycar/assets/82080194/bec8a2b9-ad7f-4e95-89c8-e7ea17b8fb6f)


## Donkey library
The JetRacer uses a Python self-driving library release 4.4.0 https://github.com/autorope/donkeycar

### Setup
To set up the JetRacer, we followed the provided guide https://www.waveshare.com/wiki/DonkeyCar_for_JetRacer_ROS_Tutorial_I:_Install_Jetson_Nano
We have decided to decrease the maximum speed by changing the PWM_STEERING_THROTTLE config values to the following: \
"THROTTLE_FORWARD_PWM": 397,            #pwm value for max forward throttle\
"THROTTLE_STOPPED_PWM": 307,            #pwm value for no movement\
"THROTTLE_REVERSE_PWM": 157,            #pwm value for max reverse throttle\
DEFAULT_MODEL_TYPE = '**safety_rnn**' # Donekycar RNN model with our safety layer implemented. Read further down for more details.

## Inputs and camera hack
The camera position of this pack does not overlook the track properly, and the quality and the lens do not provide enough context on the car's position. Therefore, we have decided to mount the camera on the top of the kit on the lidar. Due to the nature of our track, lidar could not capture certain obstacles, including lines and small boxes. Therefore, using it as a mount did not hurt our implementation. We decided to exclude lidar data in our model and went with only camera and joystick inputs.\
![IMG_1546](https://github.com/ValachPatrik/Safety-Layer-for-autonomous-driving-with-Donkeycar/assets/82080194/db48ce28-c0c4-4ab1-9529-0c873f22c210)\
![IMG_1547](https://github.com/ValachPatrik/Safety-Layer-for-autonomous-driving-with-Donkeycar/assets/82080194/fcb4a543-4170-4cd3-8268-8f22f1a5d44e)

### Model Training
As discussed in the previous section, we use the camera and joystick input to train the model.
The library requires manual training data from us, driving it on track. We tried to drive it in as accurate a manner as possible with backing up if the car were to hit anything due to its low turning angle. 
We have collected ~11k records to train the model. If there are any more records, the library trainer will take forever to train the model.

### Model Selection
We have tested the wide selection of models provided by this library, including "linear", "latent", "**rnn**", "3d".
The best for our track, with the focus on drivability and avoiding crossing lines and hitting boxes, is the **RNN** model.
This model still blunders on our track, so we implemented the safety layer. Read further down for more details.

## Safety Layer
### Virtual Track
### Updating virtual location
### Computing collision
### Recovery
## Connecting Donkey with Safety layer
## Results
## Conclusion
