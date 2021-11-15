#!/bin/bash
#

## Install ROS
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-noetic-desktop-full

## Install ROS State Publisher
sudo apt-get install ros-noetic-robot-state-publisher

## Install Gazebo
sudo apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control

## Install RVIZ
sudo apt-get install ros-noetic-rviz

## Install SLAM-Gmapping
sudo apt-get install ros-noetic-slam-gmapping

## Install TurtleBot3
sudo apt-get install ros-noetic-turtlebot3

## Install catkin
sudo apt-get install ros-noetic-catkin

## Install map_server
sudo apt-get install ros-noetic-map-server

## Install tf2-sensor-msgs
sudo apt-get install ros-noetic-tf2-sensor-msgs

## Install multirobot-map-merge
sudo apt install ros-noetic-multirobot-map-merge ros-noetic-explore-lite

## Creating a workspace for catkin
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src

## Clone Turtlebot3 Repos
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git -b noetic-devel
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git -b noetic-devel
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git -b noetic-devel

## Clone map_server Repo
git clone https://github.com/ros-planning/navigation.git -b noetic-devel

## Clone multirobot_map_merge Repo
git clone https://github.com/hrnr/m-explore.git -b noetic-devel

## Run catkin_make
cd ~/catkin_ws && catkin_make

## Append the following lines manually to ~/.bashrc
#source /opt/ros/noetic/setup.bash
#source /home/emil/catkin_ws/devel/setup.bash
#export TURTLEBOT3_MODEL=waffle_pi
#export SVGA_VGPU10=0

## Then run "source ~/.bashrc" command
