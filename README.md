# KinectBallTracking
This ROS node is written for ROB 421/521, Research Robotics, Spring 2018.
The task is to catch and throw a ball, so this node detects a ball moving in space via a Kinect depth camera.

##Subscribes
/camera/depth/image [Type: sensor_msgs/Image]

##Publishes
/ball_pos
