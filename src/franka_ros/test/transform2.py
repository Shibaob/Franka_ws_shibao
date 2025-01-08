#import pandas as pd
import numpy as np


#def quaternion_to_matrix(q):
##w x y z = q

#w=0.8961673801526222
#x=-0.3452413097944663
#y=-0.04949479770044807
#z=0.274304082657146

#return np.array([[1-2*y*y-2*z*z, 2*x*y-2*z*w, 2*x*z+2*y*w],
#                 [2*x*y+2*z*w, 1-2*x*x-2*z*z, 2*y*z-2*x*w],
#                 [2*x*z-2*y*w, 2*y*z+2*x*w, 1-2*x*x-2*y*y]])


def quaternion_to_rotation_matrix(q):  # x, y ,z ,w
    rot_matrix = np.array(
        [[1.0 - 2 * (q[1] * q[1] + q[2] * q[2]), 2 * (q[0] * q[1] - q[3] * q[2]), 2 * (q[3] * q[1] + q[0] * q[2])],
         [2 * (q[0] * q[1] + q[3] * q[2]), 1.0 - 2 * (q[0] * q[0] + q[2] * q[2]), 2 * (q[1] * q[2] - q[3] * q[0])],
         [2 * (q[0] * q[2] - q[3] * q[1]), 2 * (q[1] * q[2] + q[3] * q[0]), 1.0 - 2 * (q[0] * q[0] + q[1] * q[1])]],
        dtype=q.dtype)
    return rot_matrix
