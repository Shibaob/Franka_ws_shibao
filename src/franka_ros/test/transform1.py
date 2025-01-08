from scipy.spatial.transform import Rotation as R
 
 
def quaternion2rot(quaternion):
    r = R.from_quat(quaternion)
    rot = r.as_matrix()
    return rot
 
 
quaternion = [0.03551, 0.21960, -0.96928, 0.10494]
print(quaternion2rot(quaternion))
 

