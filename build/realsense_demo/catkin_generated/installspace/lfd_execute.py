#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import moveit_msgs.msg
import pandas as pd
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

# Initialize the ROS node
rospy.init_node('franka_trajectory_executer', anonymous=True)

# Initialize moveit_commander
moveit_commander.roscpp_initialize([])

# Instantiate RobotCommander and MoveGroupCommander
robot = moveit_commander.RobotCommander()
group = moveit_commander.MoveGroupCommander("panda_arm")

# Load joint values from the CSV file
file_path = 'promp_joint.csv'  # Replace with your file path
df = pd.read_csv(file_path, header=None)

# Create a new RobotTrajectory object
trajectory = moveit_msgs.msg.RobotTrajectory()
trajectory.joint_trajectory = JointTrajectory()
trajectory.joint_trajectory.joint_names = group.get_active_joints()

elapsed_time = rospy.Duration(0)

time_increment = rospy.Duration(1)

# Add points to the trajectory
for index, row in df.iterrows():
    point = JointTrajectoryPoint()
    point.positions = list(row)

    elapsed_time += time_increment
    point.time_from_start = elapsed_time
    
    trajectory.joint_trajectory.points.append(point)

# Execute the trajectory
group.execute(trajectory, wait=True)

# Calling `stop()` ensures that there is no residual movement
group.stop()

# Clean shutdown of moveit_commander
moveit_commander.roscpp_shutdown()
