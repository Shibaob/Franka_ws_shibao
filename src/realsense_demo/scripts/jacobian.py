#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
import urdf_parser_py.urdf
import PyKDL as kdl
from kdl_parser_py.urdf import treeFromUrdfModel

# Initialize the ROS node
rospy.init_node('kdl_jacobian_example')

# Load the URDF from the parameter server
robot_urdf = rospy.get_param('robot_description')  # Adjusted to not use leading slash for consistency
urdf = urdf_parser_py.urdf.URDF.from_xml_string(robot_urdf)

# Create a KDL tree from the URDF
(kdl_tree, _) = treeFromUrdfModel(urdf)

# Specify the base and end-effector link names
base_link = "panda_link0"
end_effector_link = "panda_link8"  # Adjust this if your robot's end-effector has a different name

# Create a KDL chain from the base to the end effector
chain = kdl_tree.getChain(base_link, end_effector_link)

# Create the solvers in PyKDL
jnt_to_jac_solver = kdl.ChainJntToJacSolver(chain)

# Create a KDL array for the joint positions
number_of_joints = chain.getNrOfJoints()
joint_positions = kdl.JntArray(number_of_joints)

# Assuming you have filled joint_positions with the current joint positions of your robot

# Create a Jacobian matrix
jacobian = kdl.Jacobian(number_of_joints)

# Calculate the Jacobian
jnt_to_jac_solver.JntToJac(joint_positions, jacobian)

# Now 'jacobian' is a PyKDL.Jacobian object containing the Jacobian matrix

# Optionally print the Jacobian matrix
for i in range(jacobian.rows()):
    for j in range(jacobian.columns()):
        print(jacobian[i, j], end=' ')
    print()
