#!/usr/bin/env python
 
import rospy
from std_msgs.msg import String
#from ros_to_deepstream.msg import video_info_msg
import sys
from franka_msgs.msg import FrankaState
#import franka_msgs

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.header)
    rospy.loginfo('Debug info')
    rospy.loginfo(data.dq)
    
    print(data.dq)
    
    
    
def listener():
 
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
 
    #rospy.Subscriber('/perception/traffic_light_recognition/output/rois', String, callback)
    rospy.Subscriber('/franka_state_controller/franka_states', FrankaState, callback)
 
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
 
if __name__ == '__main__':
    listener()
#    -0.008446809746995168, 0.7521854392269202, 0.009842913717257597, -1.2055387311688468, -0.007889835704542932, 3.4281449226230913, 0.8270649071486212)
