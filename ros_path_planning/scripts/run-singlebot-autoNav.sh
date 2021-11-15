#!/bin/bash
#

clear

# Start Gazebo and load House map
gnome-terminal --tab --command="bash -c 'roslaunch ros_path_planning single_robot.launch world_name:=wh1;'" #$SHELL'"

# Start RViz
gnome-terminal --tab --command="bash -c 'sleep 5; roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping;'" #$SHELL'"

# Automated navigation
gnome-terminal --tab --command="bash -c 'sleep 10; roslaunch turtlebot3_gazebo turtlebot3_simulation.launch;'" #$SHELL'"

# Save map
#rosrun map_server map_saver -f ~/maps/wh1_gmapping

exit
