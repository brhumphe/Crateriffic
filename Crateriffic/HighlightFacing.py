import bpy
import bmesh
from mathutils import Vector

# This extra utility function handles transforming world coordinates to normalized device coordinates
from bpy_extras.object_utils import world_to_camera_view

bl_info = {
    "name": "Crateriffic",
    "author": "Benjamin Humpherys",
    "location": "View3D > Tools > Crateriffic",
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
        mesh = bmesh.from_edit_mesh(me)
        # bm.from_mesh(me)

        mesh.faces.active = None

        cam = bpy.data.objects["Camera"]
        cam_rotation = cam.rotation_euler
        cam_dir = Vector((0, 0, 1))
        cam_dir.rotate(cam_rotation)
        print("Camera direction:", cam_dir)

        color_layer = mesh.loops.layers.color['Col']

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


        # Show the updates in the viewport
        # and recalculate n-gon tessellation.
        bmesh.update_edit_mesh(me, True)
        bpy.ops.object.mode_set(mode='OBJECT')

        return {'FINISHED'}


def register():
    bpy.utils.register_class(HighlightFacingOperator)

    print("%s registration complete" % bl_info.get("name"))


def unregister():
    bpy.utils.unregister_class(HighlightFacingOperator)

    print("%s unregistering complete" % bl_info.get("name"))


if __name__ == "__main__":
    try:
        unregister()
    except Exception as e:
        print(e)
        pass

    register()
