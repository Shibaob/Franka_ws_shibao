import rospy
from trajectory_msgs.msg import *
from control_msgs.msg import *

import actionlib
from sensor_msgs.msg import JointState
import Franka

JOINT_NAMES = ['panda_joint1', 'panda_joint2', 'panda_joint3',
               'panda_joint4', 'panda_joint5', 'panda_joint6', 'panda_joint7']

mybot = Franka.FrankArm()

camera_color_img, camera_depth_img = Franka.get_camera_data()