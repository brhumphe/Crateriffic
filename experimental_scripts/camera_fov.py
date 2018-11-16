import bpy
import bmesh

# This extra utility function handles transforming world coordinates to normalized device coordinates
from bpy_extras.object_utils import world_to_camera_view

bpy.ops.object.mode_set(mode='EDIT')
obj = bpy.context.edit_object
me = obj.data
mesh = bmesh.from_edit_mesh(me)
mesh.faces.active = None

color_layer = mesh.loops.layers.color['Col']

cam = bpy.data.objects["Camera"]


# NOTE: This does not yet correctly handle occluded geometry!
for v in mesh.verts:
    color = (1, 1, 1)

    p = world_to_camera_view(bpy.context.scene, cam, v.co)
    # Check if vertex is visible to camera
    if (0 < p.x < 1) and (0 < p.y < 1):
        # v.select = True
        # Check faces connected to vertex
        for face in v.link_faces:
            direction = face.normal - cam.location

            if direction.dot(face.normal) < 0:
                face.select = True
                color = (1, 0, 1)

    for face in v.link_faces:
        # Color faces depending on dot product direction
        for loop in face.loops:
            loop[color_layer] = color

# Write out changes
bmesh.update_edit_mesh(me, True)
bpy.ops.object.mode_set(mode='OBJECT')
