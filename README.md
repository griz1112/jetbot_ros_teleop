# jetbot_ros_teleop

** Work in progress **

** First attempt to write python code so might be inefficient but it does work

This repo consists of modifications to Dusty-NV's jetbot_ros repo. https://github.com/dusty-nv/jetbot_ros  I added a python script for teleop operation and modified jetbot_motors to accept my message format. Other than that its untouched.

This is a ROS node for use with teleop_twist_joy on a base station. You will need to set up the teleop.yaml file for that package using 1 for the turbo speed and .5 for the regular speed. Also set angular speed to 1. The two top buttons on the top of the xbox controller are deadman/speed switches. You can change this with the teleop.yaml file as well. Left switch is turbo right is regular speed. One of them has to be depressed for the jetbot to move.

Set up ROS networking between the jetbot and the base station.

On the jetbot side run rosrun jetbot_ros jetbot_motors.py and rosrun jetbot_ros jetbot_teleop.py.

On the base station side run roslaunch teleop_twist_joy teleop.launch. Be sure and edit teleop.launch and configure it for the type of controller you have. I am using an Xbox wired controller.

Push one of the speed keys and use the left joystick for forward/reverse speed and the right joystick for yaw to the left or right. 


