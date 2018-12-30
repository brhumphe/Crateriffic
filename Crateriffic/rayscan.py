import bpy
import bmesh
from mathutils import Vector
from mathutils.bvhtree import BVHTree

class RayScanOperator(bpy.types.Operator):
    bl_idname = "mesh.rayscan"
    bl_label = "Ray Scan"
    bl_options = {'REGISTER', 'UNDO'}

    count_x = bpy.props.IntProperty(name="X Samples", min=1, default=10)
    count_y = bpy.props.IntProperty(name="Y Samples", min=1, default=10)


    @classmethod
    def poll(cls, context):
        return context.object.type == 'MESH'
        # return True


    def invoke(self, context, event):
        # TODO: Change this to be the currently active mesh
        cube = bpy.data.objects['Cube']
        self.bvh = BVHTree.FromObject(cube, bpy.context.scene)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    
    def modal(self, context, event):
        v3d = context.space_data
        rv3d = v3d.region_3d

        if event.type == 'MOUSEMOVE':
            self.execute(context)
            context.area.header_text_set("Running modal")

        elif event.type == 'LEFTMOUSE':
            context.area.header_text_set()
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            context.area.header_text_set()
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}


    def execute(self, context):
        bvh = self.bvh

        # Get object data
        # TODO: Make these into properties stored extrernal to the operator
        sphere = bpy.data.objects['sphere']
        camera = bpy.data.objects['Camera']

        # Find out which direction the camera is pointing
        # TODO: Modify to cast a grid of vectors using camera.data.angle_x/y
        cam_dir = Vector((0, 0, -1))
        cam_dir.rotate(camera.rotation_euler)

        # Cast a ray towards the center of the camera view
        loc, norm, index, distance = bvh.ray_cast(camera.location, cam_dir)
        if loc is not None:
            # Move sphere to the intersection
            # TODO: Change this to drawing with bgl
            sphere.location = loc
        print(loc)

        return {'RUNNING_MODAL'}
