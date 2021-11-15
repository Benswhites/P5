#!/bin/bash
#

clear

# Start Gazebo and load House map
gnome-terminal --tab --command="bash -c 'roslaunch ros_path_planning single_robot.launch world_name:=wh1;'" #$SHELL'"

# Start RViz
gnome-terminal --tab --command="bash -c 'sleep 5; roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping;'" #$SHELL'"

# Manual navigation
gnome-terminal --tab --command="bash -c 'sleep 10; roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch;'" #$SHELL'"

# Save map
#rosrun map_server map_saver -f ~/maps/wh1_gmapping

exit
