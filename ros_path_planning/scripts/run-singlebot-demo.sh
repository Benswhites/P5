#!/bin/bash
#

clear

# Start Gazebo and load House map
gnome-terminal --tab --command="bash -c 'roslaunch ros_path_planning single_robot.launch world_name:=wh2;'" #$SHELL'"

# Start RViz
gnome-terminal --tab --command="bash -c 'sleep 5; roslaunch ros_path_planning single_nav.launch map_file:=../maps/wh1_gmapping.yaml;'" #$SHELL'"

# Run Python Code
gnome-terminal --tab --command="bash -c 'sleep 10; python3 ../python3/return_to_base.py;'"
#$SHELL'"

clear
#exit

