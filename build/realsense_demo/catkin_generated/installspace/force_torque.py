#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from franka_msgs.msg import FrankaState
from sensor_msgs.msg import JointState
import csv
import datetime

class ForceTorqueDataCollector:
    def __init__(self):
        # Initialize ROS node
        rospy.init_node('force_torque_data_collector', anonymous=True)
        
        # Subscribe to the Franka state topic and joint states topic
        self.state_sub = rospy.Subscriber("/franka_state_controller/franka_states", FrankaState, self.state_callback)
        # self.joint_sub = rospy.Subscriber("/joint_states", JointState, self.joint_callback)

        # Data storage
        self.data = []

    def state_callback(self, data):
        # Extract force and torque data
        force = data.F_T_EE[0:3]  # Force data
        torque = data.F_T_EE[3:6]  # Torque data

        # Append to data list
        self.data.append({
            'time': rospy.get_time(),
            'force_x': force[0],
            'force_y': force[1],
            'force_z': force[2],
            'torque_x': torque[0],
            'torque_y': torque[1],
            'torque_z': torque[2]
        })

    # def joint_callback(self, data):
    #     # We can process joint states data here if needed
    #     pass

    def save_data(self):
        # Save the collected data to a CSV file
        with open(f'force_torque_data_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.csv', 'w', newline='') as csvfile:
            fieldnames = ['time', 'force_x', 'force_y', 'force_z', 'torque_x', 'torque_y', 'torque_z']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for entry in self.data:
                writer.writerow(entry)

if __name__ == '__main__':
    collector = ForceTorqueDataCollector()
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    
    # Save data when the program ends
    collector.save_data()
    print("Data saved successfully")
