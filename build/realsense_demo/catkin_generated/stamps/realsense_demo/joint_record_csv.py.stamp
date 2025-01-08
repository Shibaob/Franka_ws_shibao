#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import rospy
import moveit_commander
import csv
from sensor_msgs.msg import JointState

class ArmTrajectoryRecorder(object):
    def __init__(self, group_name="panda_arm", movement_threshold=0.01):
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('record_arm_trajectory', anonymous=True)

        self.arm_group = moveit_commander.MoveGroupCommander(group_name)
        self.joint_state_subscriber = rospy.Subscriber("/joint_states", JointState, self.joint_state_callback)
        self.trajectory_data = []
        self.movement_threshold = movement_threshold
        self.last_joint_state = None
        self.recording = False

    def joint_state_callback(self, joint_state):
        if self.last_joint_state is None:
            self.last_joint_state = joint_state
            return

        # Check if the robot arm has started moving 机械臂开始启动才开始记录
        if not self.recording:
            if self.has_moved(joint_state):
                rospy.loginfo("Movement detected, starting recording...")
                self.recording = True

        if self.recording:
            # Recording joint positions, velocities, and accelerations
            self.trajectory_data.append(
                joint_state.position + joint_state.velocity + joint_state.effort
            )

    def has_moved(self, current_joint_state):
        # Calculate the difference in joint positions
        delta = [abs(c - l) for c, l in zip(current_joint_state.position, self.last_joint_state.position)]
        return any(d > self.movement_threshold for d in delta)

    def save_to_csv(self, file_name='joint_trajectory.csv'):
        rospy.loginfo('Saving arm trajectory to csv...')
        with open(file_name, 'w') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in self.trajectory_data:
                csv_writer.writerow(row)
        rospy.loginfo('Arm trajectory has been saved to ' + file_name)

    def run(self):
        rospy.spin()

if __name__ == "__main__":
    recorder = ArmTrajectoryRecorder()
    rospy.on_shutdown(recorder.save_to_csv)
    recorder.run()


