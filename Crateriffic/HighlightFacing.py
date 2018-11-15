import bpy
import bmesh
from mathutils import Vector

bl_info = {
    "name": "Crateriffic",
    "author": "Benjamin Humpherys",
    "location": "View3D > Tools > Craterrific",
    "category": "Development"
}


class HighlightFacingOperator(bpy.types.Operator):
    bl_idname = "mesh.highlight_visible"
    bl_label = "Highlight Faces who are tilted towards the camera"

    highlight_property = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return context.object.type == 'MESH'

    def invoke(self, context, event):
        print("Invoking Highlight Visible")
        # Check if a mesh object is selected
        try:
            bpy.ops.object.mode_set(mode='EDIT')
        except:
            self.report({'ERROR'}, "Must select a mesh object")
            return {'CANCELLED'}

        obj = bpy.context.edit_object
        me = obj.data

        # Get a BMesh representation
        bm = bmesh.from_edit_mesh(me)
        # bm.from_mesh(me)

        bm.faces.active = None

        cam = bpy.data.objects["Camera"]
        cam_rotation = cam.rotation_euler
        cam_dir = Vector((0, 0, 1))
        cam_dir.rotate(cam_rotation)
        print("Camera direction:", cam_dir)

        color_layer = bm.loops.layers.color['Col']

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

        return {'FINISHED'}

def register():
    bpy.utils.register_class(HighlightVisibleOpFacing

    print("%s registration complete" % bl_info.get("name"))

def unregister():
    bpy.utils.unregister_class(HighlightVisibleOpFacing

    print("%s unregistration complete" % bl_info.get("name"))

if __name__ == "__main__":
    try:
        unregister()
    except Exception as e:
        print(e)
        pass

    register()
