"""
=================
      ProMP
=================

Probabilistic Movement Primitives (ProMPs) define distributions over
trajectories that can be conditioned on viapoints. In this example, we
plot the resulting posterior distribution after conditioning on varying
start positions.
"""
print(__doc__)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from promp import ProMP

# Load the trajectory data
file_path = 'lfd_joint2.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path, header=None)
selected_data = data.iloc[:, :7]  # Select relevant columns
trajectory_np = selected_data.to_numpy()

## Get the first row from the original trajectory
first_row = trajectory_np[0]

# Initialize the ProMP
n_dims = trajectory_np.shape[1]  # Number of dimensions
promp = ProMP(n_dims=n_dims)

# Train the ProMP (assuming the weights method is used for training)
# T could be an array of time steps corresponding to each row in trajectory_np
# weig is ProMP weights by linear regression
# new_trajectory is the generate new trajectory
T = np.arange(trajectory_np.shape[0]).astype(float)
weig = promp.weights(T, trajectory_np, lmbda=1e-12)
new_trajectory = promp.trajectory_from_weights(T, weig)

new_trajectory_with_first_row = np.vstack([first_row, new_trajectory])
new_trajectory_df = pd.DataFrame(new_trajectory_with_first_row)

## save the new trajectory into a .csv file
output_file_path = 'promp_joint.csv'
new_trajectory_df.to_csv(output_file_path, index=False, header=False)


# 
# Visualization function (as defined previously)
# 
def plot_trajectory(data, title):
    num_dimensions = data.shape[1]
    time_steps = data.shape[0]
    time = np.arange(time_steps)

    plt.figure(figsize=(15, num_dimensions * 2))
    for i in range(num_dimensions):
        plt.subplot(num_dimensions, 1, i + 1)
        plt.plot(time, data[:, i])
        plt.ylabel(f'Dimension {i+1}')
        plt.grid(True)

    plt.xlabel('Time Steps')
    plt.suptitle(title)
    plt.show()


## Visualize the original and generated trajectories
# plot_trajectory(trajectory_np, "Original Trajectory")
plot_trajectory(new_trajectory_with_first_row, "ProMPs Generated Trajectory")

