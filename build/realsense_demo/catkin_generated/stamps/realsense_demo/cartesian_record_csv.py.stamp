#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import rospy
import moveit_commander
import csv
from std_msgs.msg import Header

class ArmTrajectoryRecorder(object):
    def __init__(self, group_name="panda_arm"):
        # 初始化moveit_commander和rospy
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('record_arm_trajectory', anonymous=True)

        # 初始化move group commander对象
        self.arm_group = moveit_commander.MoveGroupCommander(group_name)

        # 存储位置数据的列表
        self.position_data = []

        # 定时器启动，用于记录位置
        rospy.Timer(rospy.Duration(0.1), self.record_arm_position)

    def record_arm_position(self, event):
        # 获取当前末端执行器的位置
        current_pose = self.arm_group.get_current_pose().pose
        if not self.position_data:  # 如果列表为空，则直接添加
            self.position_data.append([
                current_pose.position.x,
                current_pose.position.y,
                current_pose.position.z
            ])
        else:  # 如果不为空，则检查与上一个点的差值
            previous_pose = self.position_data[-1]
            if (abs(current_pose.position.x - previous_pose[0]) > 0.0001 or
                    abs(current_pose.position.y - previous_pose[1]) > 0.0001 or
                    abs(current_pose.position.z - previous_pose[2]) > 0.0001):
                self.position_data.append([
                    current_pose.position.x,
                    current_pose.position.y,
                    current_pose.position.z
                ])

    def save_to_csv(self, file_name='cartesian_traj.csv'):
        # 当节点关闭时，将位置数据写入CSV文件
        rospy.loginfo('Saving arm trajectory to csv...')
        with open(file_name, 'w') as csvfile:
            csv_writer = csv.writer(csvfile)
            # 转置位置数据从3行n列
            position_data_transposed = zip(*self.position_data)
            for row in position_data_transposed:  # 写入数据
                csv_writer.writerow(row)
        rospy.loginfo('Arm trajectory has been saved to ' + file_name)

    def run(self):
        rospy.loginfo('Recording arm trajectory...')
        rospy.spin()  # 循环直到收到中断信号
        self.save_to_csv()  # 保存数据到CSV

if __name__ == "__main__":
    try:
        recorder = ArmTrajectoryRecorder(group_name="panda_arm")  # 确保这是您的planning group名称
        recorder.run()
    except rospy.ROSInterruptException:
        pass
    except KeyboardInterrupt:
        recorder.save_to_csv()  # 在中断时保存数据到CSV
        pass



