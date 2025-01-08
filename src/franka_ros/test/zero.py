import rospy
from trajectory_msgs.msg import *
from control_msgs.msg import *
import numpy as np
import actionlib
from sensor_msgs.msg import JointState
import Franka
from state import extract_groups

JOINT_NAMES = ['panda_joint1', 'panda_joint2', 'panda_joint3',
               'panda_joint4', 'panda_joint5', 'panda_joint6','panda_joint7']
 
mybot=Franka.FrankArm()
filename1 = 'pose.txt'
pos = extract_groups(filename1)
filename2 = 'vel.txt'
ve = extract_groups(filename2)
filename3 = 'acc.txt'
ac = extract_groups(filename3)
filename4 = 't.txt'
tt = extract_groups(filename4)
def move():
          #goal就是我们向发送的关节运动数据，实例化为FollowJointTrajectoryGoal()类
          goal = FollowJointTrajectoryGoal()
 
          #goal当中的trajectory就是我们要操作的，其余的Header之类的不用管
          goal.trajectory = JointTrajectory()
          #goal.trajectory底下一共还有两个成员，分别是joint_names和points，先给joint_names赋值
          goal.trajectory.joint_names = JOINT_NAMES
 
          #从joint_state话题上获取当前的关节角度值，因为后续要移动关节时第一个值要为当前的角度值
 
          #给trajectory中的第二个成员points赋值
          #points中有四个变量，positions,velocities,accelerations,effort，我们给前三个中的全部或者其中一两个赋值就行了
          point_len = len(tt)-1
          goal.trajectory.points = [0] * (point_len-1)
          for i in range(0,point_len-1):
               pose = [float(s) for s in pos[i]]
               vel = [float(s) for s in ve[i]]
               acc = [float(s) for s in ac[i]]
               t = [float(s) for s in tt[i]]
               T=0.001+t[0]
               print(t)
               goal.trajectory.points[i]=JointTrajectoryPoint(positions=pose, velocities=vel,accelerations=acc,time_from_start=rospy.Duration(T))

          #发布goal，注意这里的client还没有实例化，ros节点也没有初始化，我们在后面的程序中进行如上操作
          client.send_goal(goal)
          client.wait_for_result()
 
def pub_test():
          global client
 
          #初始化ros节点
          rospy.init_node("pub_action_test")
 
          #实例化一个action的类，命名为client，与上述client对应，话题为arm_controller/follow_joint_trajectory，消息类型为FollowJointTrajectoryAction
          client = actionlib.SimpleActionClient('effort_joint_trajectory_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
          print("Waiting for server...")
          #等待server
          client.wait_for_server()
          print("Connect to server")
          #执行move函数，发布action
          move()
 
if __name__ == "__main__":
          pub_test()
