#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import PoseStamped
import numpy as np

class PoseRecorder:
    def __init__(self, topic_name='/robot_end_effector_pose', threshold=0.01):
        rospy.init_node('pose_recorder', anonymous=True)
        self.subscriber = rospy.Subscriber(topic_name, PoseStamped, self.callback)
        self.poses = []
        self.last_recorded_pose = None
        self.threshold = threshold
        rospy.on_shutdown(self.on_shutdown)

    def pose_changed(self, current_pose, last_pose):
        if last_pose is None:
            return True
        current_position = np.array([current_pose.position.x, current_pose.position.y, current_pose.position.z])
        last_position = np.array([last_pose.position.x, last_pose.position.y, last_pose.position.z])
        return np.linalg.norm(current_position - last_position) > self.threshold

    def callback(self, data):
        current_pose = data.pose
        if self.pose_changed(current_pose, self.last_recorded_pose):
            rospy.loginfo('Pose changed')
            self.poses.append(current_pose)
            self.last_recorded_pose = current_pose

    def record_poses(self):
        rospy.loginfo('Starting to record poses...')
        rospy.spin()

    def on_shutdown(self):
        rospy.loginfo('Shutting down, saving recorded poses...')
        if self.poses:  # Check if there is something to save
            # Assuming poses are geometry_msgs/PoseStamped or similar, adjust as necessary
            positions = [{'x': pose.position.x, 'y': pose.position.y, 'z': pose.position.z} for pose in self.poses]
            orientations = [{'x': pose.orientation.x, 'y': pose.orientation.y, 'z': pose.orientation.z, 'w': pose.orientation.w} for pose in self.poses]
            np.savez_compressed('poses.npz', positions=positions, orientations=orientations)
            rospy.loginfo('Poses have been recorded and saved.')

if __name__ == '__main__':
    recorder = PoseRecorder()
    recorder.record_poses()
