# Camera stuff
import bpy
import numpy as np

cam = bpy.data.objects["Camera"]

# QUESTION: Does the axis of rotation match the camera direction?
# Quaternion seems not to update until selected in UI?
cam_axis = cam.rotation_quaternion.to_axis_angle()[0]

# Maybe this approach is better
# Camera points along -Z axis, so rotate that using rotation matrix
cam_rotation_matrix = np.array(cam.rotation_euler.to_matrix())
cam_dir = cam_rotation_matrix.dot(np.array([0,0,-1]))

# Camera perspective matrix
c_matrix = cam.calc_matrix_camera()