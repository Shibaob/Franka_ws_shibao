#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import rospy
import moveit_commander
import numpy as np
from geometry_msgs.msg import PoseStamped, Pose
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from realsense_demo.srv import ExecuteTrajectory, ExecuteTrajectoryResponse 

class MoveRobot():
    def __init__(self):
        # 初始化moveit_commander和rospy
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('move_robot', anonymous=True)

        # 初始化robot commander对象
        self.robot = moveit_commander.RobotCommander()

        # 初始化move group commander对象
        self.arm_group = moveit_commander.MoveGroupCommander("panda_arm")

        # 设置机械手臂的速度和加速度
        self.arm_group.set_max_acceleration_scaling_factor(1)
        self.arm_group.set_max_velocity_scaling_factor(1)

    def plan_cartesian_path(self, waypoints):
        # 设置机器臂当前的状态作为运动初始状态
        self.arm_group.set_start_state_to_current_state()

        fraction = 0.0   # 路径规划覆盖率
        maxtries = 100   # 最大尝试规划次数
        attempts = 0     # 已经尝试规划次数

        # 尝试规划一条笛卡尔空间下的路径，依次通过所有路点
        while fraction < 1.0 and attempts < maxtries:
            (plan, fraction) = self.arm_group.compute_cartesian_path(
                waypoints,  # waypoint poses
                0.01,       # eef_step
                0.0,        # jump_threshold
                False       # avoid_collisions
            )
            attempts += 1

        if fraction > 0.9:
            rospy.loginfo("Path computed successfully. Moving the arm.")
            self.arm_group.execute(plan, wait=True)
            rospy.loginfo("Path execution complete.")
        else:
            rospy.loginfo("Path planning failed with only " + str(fraction) + " success after " + str(attempts) + " attempts.")

    def add_waypoints(self, reference_trajectory):
        waypoints = []
        for i in range(reference_trajectory.shape[1]):
            pose = Pose()
            pose.position.x = reference_trajectory[0, i]
            pose.position.y = reference_trajectory[1, i]
            pose.position.z = reference_trajectory[2, i]
            pose.orientation.x = -0.9239194436233638
            pose.orientation.y = 0.3825865154249364
            pose.orientation.z = -0.0006053749923593257
            pose.orientation.w = 0.0002311510706435422
            waypoints.append(pose)
        return waypoints

    def execute_trajectory_service(self, req):
        try:
            filename = '/home/pengcheng-robot/MPs_ws/traj/{}.csv'.format(req.index)
            reference_trajectory = np.loadtxt(filename, delimiter=',')
            waypoints = self.add_waypoints(reference_trajectory)
            self.plan_cartesian_path(waypoints)
            return ExecuteTrajectoryResponse()
        except Exception as e:
            rospy.logerr("Error executing trajectory: %s" % str(e))
            return ExecuteTrajectoryResponse()

def main():
    try:
        rospy.loginfo('Starting MoveRobot Node')
        moverobot = MoveRobot()

        s = rospy.Service('execute_trajectory', ExecuteTrajectory, moverobot.execute_trajectory_service)
        rospy.loginfo("Service server has been started.")

        rospy.spin()

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()