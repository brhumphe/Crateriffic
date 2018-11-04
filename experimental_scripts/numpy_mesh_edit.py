import numpy as np
import bpy


def get_co(ob):
    """Gets vertex locations from ob and returns them in 
    an Nx3 numpy array"""
    v_count = len(ob.data.vertices)
    co = np.zeros(v_count * 3, dtype=np.float64)
    # Write vertex data into numpy array
    ob.data.vertices.foreach_get('co', co)
    co.shape = (v_count, 3)
    return co


def get_normals(ob):
    """Gets polygon normals from ob as Nx3 numpy array"""
    n_count = len(ob.data.polygons)
    norms = np.zeros(n_count * 3, dtype=np.float64)
    ob.data.polygons.foreach_get("normal", norms)
    norms.shape = (n_count, 3)
    return norms


print("Running numpy_mesh_edit.py")

obj = bpy.context.object
verts = get_co(obj)
normals = get_normals(obj)
# co[:,0] -= 1
# print(co[:10])

cam = bpy.data.objects["Camera"]
# Camera points along -Z axis, so rotate that using rotation matrix
cam_rotation_matrix = np.array(cam.rotation_euler.to_matrix())
cam_dir = cam_rotation_matrix.dot(np.array([0, 0, -1]))
np_dot = np.dot(normals, cam_dir)
facing = np_dot < 0

# Set data from numpy array
obj.data.vertices.foreach_set('co', verts.ravel())

# Can't select directly: read-only property
# obj.data.polygons.foreach_set('select', facing.ravel())
obj.data.update()
