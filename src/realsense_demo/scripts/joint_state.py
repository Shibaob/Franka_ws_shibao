#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from moveit_msgs.msg import RobotTrajectory, Grasp, PlaceLocation, Constraints
from sensor_msgs.msg import JointState
## END_SUB_TUTORIAL

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
robot = moveit_commander.RobotCommander()

group_name = "panda_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)

# current joint values and pose
# print(move_group.get_current_joint_values())
# print(move_group.get_current_pose().pose)

# joint_goal = [-0.00017, -0.78558, 0.00006, -2.35601, 0.00002, 1.57161, 0.78538] # initial joints
# robot arm moves to the goal joint state
joint_goal = move_group.get_current_joint_values()
# joint_goal[0] = -0.09710210646870741
# joint_goal[1] = 0.14022892195670564
# joint_goal[2] = -0.9363551844333426
# joint_goal[3] = -2.057766297941847
# joint_goal[4] = 0.1336904613169746
# joint_goal[5] = 2.1374147936139565
# joint_goal[6] = -0.3160219769148445
joint_goal[0] = -0.53239
joint_goal[1] = 0.0951
joint_goal[2] = -0.48442
joint_goal[3] = -2.05928
joint_goal[4] = 0.05252
joint_goal[5] = 2.14308
joint_goal[6] = -0.25856


move_group.go(joint_goal, wait=True)
move_group.stop()

# move_group.set_joint_value_target(joint_goal)
# plan = RobotTrajectory()
# print(plan)