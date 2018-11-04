import bmesh
import bpy

obj = bpy.context.object

bm = bmesh.new()
bm.from_mesh(obj.data)
color_layer = bm.loops.layers.color['Col']

for face in bm.faces:
    for loop in face.loops:
        loop[color_layer] = (1, 1, 0)

bm.to_mesh(obj.data)
for area in bpy.context.screen.areas:
    if area.type in ['IMAGE_EDITOR', 'VIEW_3D']:
        area.tag_redraw()
