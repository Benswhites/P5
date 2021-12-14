# Stage 3: Physical robots (Turtlebot3 burgers)

Stage 3 is implementing the physical robots.
The ROBOTIS Turtlebot3 burgers have been used here. The theory is ot implement the code from stage 2 1:1 as the simulated robots correspond to the real robots. There were a few things that needed to be changed, such as simulated time and various robot descriptions. And the fact that it did not need to be simulated.
The bringup code consists of 2 files just like the previous stage:
make_robot.launch and tb3_bringup_nav.launch
The make_robot.launch is a general file that is called for each robot. This creates a navstack on each robot with different namespaces.
The tb3_bringup_nav.launch is where the map_server is opened as well as the setting the namespaces for the robots. Rviz is also opened here with a specific configuration.
