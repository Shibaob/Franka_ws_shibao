import rospy
from trajectory_msgs.msg import *
from control_msgs.msg import *
import numpy as np
import actionlib
from sensor_msgs.msg import JointState
import Franka
from math import pi

JOINT_NAMES = ['panda_joint1', 'panda_joint2', 'panda_joint3',
               'panda_joint4', 'panda_joint5', 'panda_joint6','panda_joint7']
 
mybot=Franka.FrankArm()
def move(x,y,z):
          #goal就是我们向发送的关节运动数据，实例化为FollowJointTrajectoryGoal()类
          goal = FollowJointTrajectoryGoal()
 
          #goal当中的trajectory就是我们要操作的，其余的Header之类的不用管
          goal.trajectory = JointTrajectory()
          #goal.trajectory底下一共还有两个成员，分别是joint_names和points，先给joint_names赋值
          goal.trajectory.joint_names = JOINT_NAMES
 
          #从joint_state话题上获取当前的关节角度值，因为后续要移动关节时第一个值要为当前的角度值
          joint_states = rospy.wait_for_message("joint_states",JointState)
          joints_pos = joint_states.position
          qInit = joints_pos[:7]
 
          #给trajectory中的第二个成员points赋值
          #points中有四个变量，positions,velocities,accelerations,effort，我们给前三个中的全部或者其中一两个赋值就行了
          goal.trajectory.points=[0]*2
          
          goal.trajectory.points[0]=JointTrajectoryPoint(positions=joints_pos, velocities=[0]*7,time_from_start=rospy.Duration(0.0))
          t1,j1 = mybot.ForwardKin(qInit)
          b1 = t1[-1]
          pose = [1.5707963267948, -0.8481508460237732, 0, -2.4425969022940386, 0, 1.5707963, 0.78539816]
          t2,j2 = mybot.ForwardKin(pose)
          print('t2', t2)

          # x = 0;
          # y = 0.588833217;
          # z = 0.248218376;


          Hgoal = np.array([[np.sin(pi/4), np.cos(pi/4), 0, x],
                            [np.cos(pi/4), -np.sin(pi/4), 0, y],
                            [0, 0, -1, z],
                            [0, 0, 0, 1]])                                   #末端姿态不变，位置变，变位置只需要改最后一列矩阵的xyz
            
          
#          Hgoal = np.array([[0.706909047, -0.706909042, -0.0236475517, 0],
#                            [-0.707106779, -0.707106779, 0, 0.288833217],
#                            [-0.0167213442, 0.0167213441, -0.999720358, 0.568218376], 
#                            [0, 0, 0, 1]])                                  #末端姿态不变，位置变，变位置只需要改最后一列矩阵的xyz
        
          
          #Hgoal = np.array([[0.706909047, -0.706909042, -0.0236475517, 0.288833217],
          #                  [-0.707106779, -0.707106779, 0, 0],
          #                  [-0.0167213442, 0.0167213441, -0.999720358, 0.568218376], 
          #                  [0, 0, 0, 1]])                                  #末端姿态不变，位置变，位姿对着d435
                                                                            #位置不变的矩阵（最后一列）为[0.288833217, 0, 0.568218376, 1]
         
      
          joint,a = mybot.IterInvKin(pose,Hgoal)
          
          print('joint', joint)
          goal.trajectory.points[1]=JointTrajectoryPoint(positions=joint, velocities=[0]*7,time_from_start=rospy.Duration(3.0))

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
          move(0,0.588833217,0.348218376)
 
if __name__ == "__main__":
          pub_test()
