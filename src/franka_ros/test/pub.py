#!/usr/bin/env python
# license removed for brevity
import rospy
from franka_gripper.msg import GraspGoal
import numpy as np

def talker():
    pub = rospy.Publisher('/franka_gripper/grasp/goal', GraspGoal, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
  #      hello_str = "goal:{width:0.03, epsilon:{ inner: 0.005, outer: 0.005},speed:0.1, force:5.0}" % rospy.get_time()
        #hello_str = ['width' ,0.03 , 'epsilon',0.05, 'speed',0.1, 'force',5.0]
        hello_str = (0.03, (0.005,0.005), 0.1, 5.0)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
