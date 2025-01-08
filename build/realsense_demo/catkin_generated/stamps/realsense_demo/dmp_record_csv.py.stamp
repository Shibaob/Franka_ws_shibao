#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import rospy
import moveit_commander
import csv
from geometry_msgs.msg import PoseStamped

class FrankaArmTrajectoryRecorder(object):
    def __init__(self, group_name="panda_arm"):
        # Initialize moveit_commander and rospy
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('record_franka_arm_trajectory', anonymous=True)

        # Initialize move group for Franka
        self.arm_group = moveit_commander.MoveGroupCommander(group_name)

        # List to store position data
        self.position_data = []

        # Timer to record position at regular intervals
        rospy.Timer(rospy.Duration(0.005), self.record_arm_position)

    def record_arm_position(self, event):
        # Get the current end-effector pose
        current_pose = self.arm_group.get_current_pose().pose
        if not self.position_data or self.is_significant_change(current_pose, self.position_data[-1]):
            self.position_data.append([
                current_pose.position.x,
                current_pose.position.y,
                current_pose.position.z
            ])

    def is_significant_change(self, current_pose, last_pose):
        # Check for significant change in position
        return (abs(current_pose.position.x - last_pose[0]) > 0.0001 or
                abs(current_pose.position.y - last_pose[1]) > 0.0001 or
                abs(current_pose.position.z - last_pose[2]) > 0.0001)

    def save_to_csv(self, file_name='cartesian_traj.csv'):
        rospy.loginfo('Saving Franka arm trajectory to csv...')
        with open(file_name, 'w') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Assuming each element in self.position_data is a list [x, y, z]
            # The following will transpose the list of positions into a format
            # where each position set [x, y, z] is in its own column
            position_data_transposed = zip(*self.position_data)
            for row in position_data_transposed:
                csv_writer.writerow(row)
        rospy.loginfo('Franka arm trajectory saved to ' + file_name)




    def run(self):
        rospy.loginfo('Recording Franka arm trajectory...')
        rospy.spin()  # Keep running until interrupted
        self.save_to_csv()

if __name__ == "__main__":
    try:
        recorder = FrankaArmTrajectoryRecorder(group_name="panda_arm")  # Ensure this is your planning group name
        recorder.run()
    except rospy.ROSInterruptException:
        pass
    except KeyboardInterrupt:
        recorder.save_to_csv()
