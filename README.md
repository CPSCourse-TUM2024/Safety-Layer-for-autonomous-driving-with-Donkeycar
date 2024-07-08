# Safety-Layer-for-autonomous-driving-with-Donkeycar
This project was created for the Embedded Systems, Cyber-Physical Systems and Robotics course.\
Created by Yigit Ilk, Roman Mishchuk, Liam Paul Brandt, Patrik Valach, Michał Chrzanowski, Paul Hagner.\
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
To set up the JetRacer, we followed the provided guide https://www.waveshare.com/wiki/DonkeyCar_for_JetRacer_ROS_Tutorial_I:_Install_Jetson_Nano \
We installed the neccesary ROS and python software. \
It was decided to decrease the maximum speed by changing the PWM_STEERING_THROTTLE config file of "mycar" folder values to the following: \
"THROTTLE_FORWARD_PWM": 397,            #pwm value for max forward throttle\
"THROTTLE_STOPPED_PWM": 307,            #pwm value for no movement\
"THROTTLE_REVERSE_PWM": 157,            #pwm value for max reverse throttle\
\
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
As previously mentioned we have added a safety layer to the DonkeyCar library by adding a special class on the RNN model implementation.
The layer ensures the car never hits any object on our track and does not cross any lines in case the model would lead it to.

### Virtual Track
The virtual track is created using the virtual_env_creator.py script. This output CSV must then be put inside the car folder in the JetRacer.
It creates a 2D map with 0 and 1 values, with 0 representing empty space and 1 representing an obstacle. The accuracy of the map is 5mm in real world per pixel in the virtual track.
The car's position is then mapped to this virtual by rounding.

### IMU tracking
$$$$$$$$$$$$$$$$$$$$$$LIAM HOW DID YOU AND CEM HACK IT

### Updating virtual location
We gather the position and heading from the odometer and then compute the car's x, y, and heading, using math formulas that can be found in the code base, to keep these values updated. Then, we map them to the virtual track to use in the actual use-case of the safety layer

### Computing collision
The objects on the virtual track and the car itself have computed collision circles, and if any of them collide, the recovery logic is called. The circle of the car has a diameter of 11mm. The circles are purposefully a bit bigger in order to stop the car before it actually hits/crosses an obstacle.

### Recovery
Once a collision is detected, the car proceeds with the recovery mode. This logic proceeds as follows :\
Wait for a few seconds. 
Reverse (If a collision is detected again, stop the reverse.)\
Wait for a few more seconds.\
Continue normal operations.\
\
This logic should keep the car safe from hitting any obstacles or lines and allow the model to retry a different approach on how to proceed.

## Connecting Donkey with Safety Layer
How did we actually connect these two things? We added a class in the DonkeyCar library for our use case. When loading the model, we chose our hacked in class instead. In this class, we have the safety logic implemented by wrapping the original run function and adding our functionality next to it. We import the safety.py file with the class implementing the virtual track and call on its function as necessary to ensure the model does not do anything incorrectly. 

On top of this, we have a tool that sends the visualisation of the virtual track and the car's location to the defined IP address on which this client should run for debugging purposes. This connection is established using the class in common_state.py that is once again located in the "mycar" folder.
$$$$$$$$$$$$$$$$$$insert image of the visualization

## Results
As a result of all these actions, the car can drive on the track we tested on. When the model is insufficient for this task, the safety layer proceeds to save the car from these unwanted actions and recovers from them. 

$$$$$$$$$$$$$$$$$$INSERT VIDEO

## Conclusion

## How to run
Proceed to set the JetRacer as defined in the product documentation.
Change up the following files:
/mycar/...

/projects/donkeycar/donkeycar/parts/
...
