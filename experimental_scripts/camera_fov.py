import bpy
import bmesh

# This extra utility function handles transforming world coordinates to normalized device coordinates
from bpy_extras.object_utils import world_to_camera_view


obj = bpy.context.edit_object
me = obj.data
mesh = bmesh.from_edit_mesh(me)
mesh.faces.active = None

cam = bpy.data.objects["Camera"]

for v in mesh.verts:
    p = world_to_camera_view(bpy.context.scene, cam, v.co)
    if (0 < p.x < 1) and (0 < p.y < 1):
        v.select = True

# Write out changes
bmesh.update_edit_mesh(me, True)
# bpy.ops.object.mode_set(mode='OBJECT')
