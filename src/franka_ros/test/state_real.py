from trajectory_msgs.msg import *
from control_msgs.msg import *
import rospy
import actionlib
import Franka
from state import extract_groups
import numpy as np

JOINT_NAMES = ['panda_joint1', 'panda_joint2', 'panda_joint3',
               'panda_joint4', 'panda_joint5', 'panda_joint6', 'panda_joint7']

mybot = Franka.FrankArm()
filename1 = 'pose.txt'
pos = extract_groups(filename1)
filename2 = 'vel.txt'
ve = extract_groups(filename2)
filename3 = 'acc.txt'
ac = extract_groups(filename3)
filename4 = 't.txt'
tt = extract_groups(filename4)
global client
rospy.init_node("pub_action_test")
client = actionlib.SimpleActionClient('effort_joint_trajectory_controller/follow_joint_trajectory',FollowJointTrajectoryAction)
client.wait_for_server()
print("Connect to server")
goal = FollowJointTrajectoryGoal()
goal.trajectory = JointTrajectory()
goal.trajectory.joint_names = JOINT_NAMES
point_len = len(tt)-1
goal.trajectory.points = [0] * point_len
for i in range(point_len-1):
     pose = [float(s) for s in pos[i]]
     vel = [float(s) for s in ve[i]]
     acc = [float(s) for s in ac[i]]
     t = [float(s) for s in tt[i]]
     T=1+t[0]
     print(t)
     #print(T)
     goal.trajectory.points[i] = JointTrajectoryPoint(positions=pose, velocities=vel,accelerations=acc,time_from_start=rospy.Duration(T))
print(goal)
client.send_goal(goal)
