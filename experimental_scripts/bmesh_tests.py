# This example assumes we have a mesh object in edit-mode

import bpy
import bmesh

# Get the active mesh
from mathutils import Vector

bpy.ops.object.mode_set(mode='EDIT')
obj = bpy.context.edit_object
me = obj.data

# Get a BMesh representation
bm = bmesh.from_edit_mesh(me)
# bm.from_mesh(me)

bm.faces.active = None
# bpy.ops.mesh.hide(unselected=False)
# bpy.context.space_data.use_occlude_geometry = True


# Useful properties
# bm.faces[150].normal  # -> Vector()
# bm.faces[150].select = True  # Set a face selected
# bpy.ops.mesh.hide(unselected=True)


cam = bpy.data.objects["Camera"]
cam_rotation = cam.rotation_euler
cam_dir = Vector((0, 0, 1))
cam_dir.rotate(cam_rotation)
print("Camera direction:", cam_dir)

color_layer = bm.loops.layers.color['Col']

# for vert in bm.verts:
#     direction = vert.co - cam.location
#     if direction.dot(vert.normal) < 0:
#         vert.select = True
#         for face in vert.link_faces:
#             face.select = True
#             for loop in face.loops:
#                 loop[color_layer] = (1, 0, 1)

for face in bm.faces:
    direction = face.normal - cam.location
    if direction.dot(face.normal) < 0:
        # face.select = True
        color = (1, 0, 1)
    else:
        color = (1, 1, 1)

    for loop in face.loops:
        loop[color_layer] = color

# Show the updates in the viewport
# and recalculate n-gon tessellation.
bmesh.update_edit_mesh(me, True)
bpy.ops.object.mode_set(mode='OBJECT')
