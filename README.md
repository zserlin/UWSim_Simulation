# UWSim_Simulation

This repo has 4 folders that go in four seperate folders in the ROS structure. 

The NEXXUS_ROV folder houses the URDF file for the ROV. It should be put in two places. The first is:

```~/opt/ros/kinetic/share/urdf_tutorial``` 

folder. This will allow ros to access it from "anywhere."

The second place it should be put is 

```~/catkin_ws/src```

The Kinematic_Scenes file holds files that should be put in the:

```~/catkin_ws/src/underwater_simulation/uwsim/data/scenes```

and

```~catkin_ws/install_isolated/share/uwsim/data``` 

folders. Putting them in the src allows them to be compiled but we have been editing the install file directly so the most recent simulation will be able to be edited there. It may be useful to update the xacro file later. 

The
