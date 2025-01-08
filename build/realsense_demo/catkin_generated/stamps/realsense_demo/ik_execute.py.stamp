#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
import actionlib
import numpy as np
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from sensor_msgs.msg import JointState

class MotionPlanning:
    def __init__(self, joint_names):
        # 初始化节点
        rospy.init_node('panda_arm_trajectory_client')

        # 初始化关节名称
        self.joint_names = joint_names
        # 连接到动作服务器
        self.client = actionlib.SimpleActionClient('/panda_arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
        rospy.loginfo("Waiting for follow_joint_trajectory server...")
        self.client.wait_for_server()
        rospy.loginfo("Connected to follow_joint_trajectory server")

        # 初始化当前关节状态为None
        self.current_joint_states = None
        # 订阅关节状态
        rospy.Subscriber("/joint_states", JointState, self.joint_states_callback)

    # 关节状态的回调函数
    def joint_states_callback(self, msg):
        self.current_joint_states = msg

    # 获取当前关节位置
    def get_current_joint_positions(self):
        if self.current_joint_states:
            arm_positions = []
            # 确保顺序与joint_names一致
            for name in self.joint_names:
                if name in self.current_joint_states.name:
                    index = self.current_joint_states.name.index(name)
                    arm_positions.append(self.current_joint_states.position[index])
            return arm_positions
        else:
            rospy.logwarn("Current joint states not yet received")
            return None

    # 规划从当前位置到目标位置的轨迹
    def plan(self, start_positions, target_positions, steps=20):
        start_positions = np.array(start_positions)
        target_positions = np.array(target_positions)
        # 线性插值计算轨迹点
        trajectory = [start_positions + (target_positions - start_positions) * step / float(steps) for step in range(1, steps + 1)]
        return trajectory

    # 计算每个轨迹点的时间
    def calculate_time_from_start(self, start_positions, target_positions, steps, max_velocity=2.1750, max_acceleration=3.75):
        distances = np.abs(np.array(target_positions) - np.array(start_positions))
        max_distance = np.max(distances)
        # 根据最大速度和加速度计算所需时间
        accel_time = max_velocity / max_acceleration
        accel_distance = 0.5 * max_acceleration * accel_time ** 2
        if max_distance <= 2 * accel_distance:
            total_time = np.sqrt(4 * max_distance / max_acceleration)
        else:
            cruise_distance = max_distance - 2 * accel_distance
            cruise_time = cruise_distance / max_velocity
            total_time = 2 * accel_time + cruise_time
        # 等间隔分配时间给每个轨迹点
        times = np.linspace(0, total_time, steps + 1)[1:]
        return times

    # 发送轨迹到动作服务器
    def send_trajectory(self, trajectory_points, times):
        goal = FollowJointTrajectoryGoal()
        goal.trajectory.joint_names = self.joint_names
        for positions, time in zip(trajectory_points, times):
            point = JointTrajectoryPoint()
            point.positions = positions
            point.time_from_start = rospy.Duration(time)
            goal.trajectory.points.append(point)
        self.client.send_goal(goal)
        self.client.wait_for_result()

    # 执行从当前位置到目标位置的移动
    def execute(self, target_positions):
        current_positions = self.get_current_joint_positions()
        if current_positions:
            steps = 20
            # 计算轨迹点和时间
            trajectory_points = self.plan(current_positions, target_positions, steps)
            times = self.calculate_time_from_start(current_positions, target_positions, steps)
            # 发送轨迹
            self.send_trajectory(trajectory_points, times)
        else:
            rospy.logwarn("Failed to get current joint positions")

if __name__ == "__main__":
    # 定义机械臂关节名称
    joint_names = ["panda_joint1", "panda_joint2", "panda_joint3", "panda_joint4", "panda_joint5", "panda_joint6", "panda_joint7"]
    # 创建规划
    mp = MotionPlanning(joint_names)
    rospy.sleep(2) 

    target_positions = [-0.1, 0.1, 0.0, -1.2, 0.0, 1.2, 0.8]  # 输入逆解决求的角度
    mp.execute(target_positions)
