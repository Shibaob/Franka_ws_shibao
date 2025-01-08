#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import math
import matplotlib.pyplot as plt

def approach_singularity():
    # Initialize the ROS node
    rospy.init_node('approach_singularity', anonymous=True)

    # Create a MoveIt commander for the Franka robot arm
    robot = moveit_commander.RobotCommander()
    group_name = 'panda_arm'
    group = moveit_commander.MoveGroupCommander(group_name)

    # Set the reference frame and end-effector link
    group.set_pose_reference_frame('panda_link0')
    group.set_end_effector_link('panda_link8')

    # Set the maximum velocity and acceleration scaling factors
    group.set_max_velocity_scaling_factor(0.5)
    group.set_max_acceleration_scaling_factor(0.5)

    # Define the joint angles for a singular configuration
    singular_joint_angles = [0, -math.pi/4, 0, -3*math.pi/4, 0, math.pi/2, 0]

    # Set the target joint angles
    group.set_joint_value_target(singular_joint_angles)

    # Plan the motion
    plan = group.plan()

    if plan.joint_trajectory.points:
        rospy.loginfo("Motion plan generated successfully.")

        # Extract the joint positions and velocities from the planned trajectory
        joint_names = plan.joint_trajectory.joint_names
        points = plan.joint_trajectory.points

        timestamps = []
        joint_positions = {name: [] for name in joint_names}
        joint_velocities = {name: [] for name in joint_names}

        for point in points:
            timestamps.append(point.time_from_start.to_sec())
            for i, name in enumerate(joint_names):
                joint_positions[name].append(point.positions[i])
                joint_velocities[name].append(point.velocities[i])

        # Execute the motion
        group.execute(plan, wait=True)
        rospy.loginfo("Robot approached singularity.")

        # Plot the joint positions and velocities over time
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

        for name in joint_names:
            ax1.plot(timestamps, joint_positions[name], label=name)
            ax2.plot(timestamps, joint_velocities[name], label=name)

        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Joint Position (rad)')
        ax1.set_title('Joint Positions over Time')
        ax1.legend()

        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Joint Velocity (rad/s)')
        ax2.set_title('Joint Velocities over Time')
        ax2.legend()

        plt.tight_layout()
        plt.show()

    else:
        rospy.logerr("Failed to generate a motion plan.")

    # Shutdown the MoveIt commander
    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    try:
        approach_singularity()
    except rospy.ROSInterruptException:
        pass