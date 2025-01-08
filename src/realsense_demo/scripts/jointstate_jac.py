#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import JointState

class JointStateListener:
    def __init__(self):
        rospy.init_node('joint_state_listener', anonymous=True)
        self.joint_angles = None
        rospy.Subscriber("/joint_states", JointState, self.joint_state_callback)
    
    def joint_state_callback(self, msg):
        self.joint_angles = msg.position  # Assuming the order of joints matches

    def get_joint_angles(self):
        return self.joint_angles

if __name__ == "__main__":
    listener = JointStateListener()
    rospy.spin()  # Keep the node running to listen for messages on the topic
    # Use listener.get_joint_angles() to access the joint angles
