#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import JointState
import numpy as np

class JointStateRecorder:
    def __init__(self, topic_name='/joint_states', threshold=0.07):
        rospy.init_node('joint_state_recorder', anonymous=True)
        self.subscriber = rospy.Subscriber(topic_name, JointState, self.callback)
        self.joint_states = []
        self.last_recorded_state = None
        self.threshold = threshold
        rospy.on_shutdown(self.on_shutdown)

    def state_changed(self, current_state, last_state):
        if last_state is None:
            return True
        current_state = np.concatenate((np.array(current_state[0]).flatten(), np.array(current_state[1]).flatten()))
        last_state = np.concatenate((np.array(last_state[0]).flatten(), np.array(last_state[1]).flatten()))
        return np.linalg.norm(current_state - last_state) > self.threshold

    def callback(self, data):
        current_state = (np.array(data.position).flatten(), np.array(data.velocity).flatten(), rospy.get_time())
        if self.state_changed(current_state, self.last_recorded_state):
            rospy.loginfo('Joint state changed')
            self.joint_states.append(current_state)
            self.last_recorded_state = current_state

    def record_joint_states(self):
        rospy.loginfo('Starting to record joint states...')
        rospy.spin()

    def on_shutdown(self):
        rospy.loginfo('Shutting down, saving recorded joint states...')
        if self.joint_states:  # Check if there is something to save
            positions = [state[0] for state in self.joint_states]
            velocities = [state[1] for state in self.joint_states]
            timestamps = [state[2] for state in self.joint_states]
            np.savez_compressed('joint_states.npz', positions=positions, velocities=velocities, timestamps=timestamps)
            rospy.loginfo('Joint states have been recorded and saved.')

if __name__ == '__main__':
    recorder = JointStateRecorder()
    recorder.record_joint_states()
