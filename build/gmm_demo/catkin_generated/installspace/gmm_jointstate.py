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
rospy.init_node('gmm_move_group', anonymous=True)
robot = moveit_commander.RobotCommander()

group_name = "panda_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)

# print(move_group.get_current_joint_values())
# print(move_group.get_current_pose().pose)

# move_group.set_named_target("home")
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 0.00018287614028711374
joint_goal[1] = -0.7855800156361434
joint_goal[2] = 2.8487011616284974e-05
joint_goal[3] = -2.356011901485206
joint_goal[4] = -8.089487758766722e-06
joint_goal[5] = 1.5716021581879938
joint_goal[6] = 0.78539495289857

move_group.go(joint_goal, wait=True)
move_group.stop()

# move_group.set_joint_value_target(joint_goal)
# plan = RobotTrajectory()
# print(plan)