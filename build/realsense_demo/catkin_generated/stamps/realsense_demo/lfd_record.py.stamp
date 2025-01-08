#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
import csv
from sensor_msgs.msg import JointState
import numpy as np

class JointStateRecorder:
    def __init__(self, threshold=0.01):
        # Initialize the ROS node
        rospy.init_node('joint_state_recorder', anonymous=True)

        # Subscribe to the joint states topic
        self.subscriber = rospy.Subscriber('/franka_state_controller/joint_states', JointState, self.callback)

        # Initialize a list to store joint states and set the threshold
        self.joint_states = []
        self.last_recorded_state = None
        self.threshold = threshold

    def state_changed(self, current_state, last_state):
        # Check if the state has changed significantly 检查机械臂是否动了
        if last_state is None:
            return True
        return np.linalg.norm(np.array(current_state) - np.array(last_state)) > self.threshold

    def callback(self, data):
        # This function is called every time a new message is published on the joint_states topic
        current_state = data.position

        if self.state_changed(current_state, self.last_recorded_state):
            # rospy.loginfo(f'Joint state changed: {current_state}')
            rospy.loginfo(f'Joint state get changed')
            self.joint_states.append(current_state)
            self.last_recorded_state = current_state

    def record_joint_states(self):
        try:
            rospy.spin()
        except KeyboardInterrupt:
            print('Recording stopped')

        # Save the recorded joint states to a CSV file
        with open('lfd_joint.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # writer.writerow(['Position'])
            for state in self.joint_states:
                writer.writerow(state)

if __name__ == '__main__':
    recorder = JointStateRecorder()
    recorder.record_joint_states()