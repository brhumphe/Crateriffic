import bpy
import bgl
import bmesh
from bpy_extras.view3d_utils import location_3d_to_region_2d
from mathutils import Vector
from mathutils.bvhtree import BVHTree

class RayScanOperator(bpy.types.Operator):
    bl_idname = "mesh.rayscan"
    bl_label = "Ray Scan"
    bl_options = {'REGISTER', 'UNDO'}

    count_x = bpy.props.IntProperty(name="X Samples", min=1, default=10)
    count_y = bpy.props.IntProperty(name="Y Samples", min=1, default=10)

    points = []

    @classmethod
    def poll(cls, context):
        return context.object.type == 'MESH'


    def invoke(self, context, event):
        if context.object.type != 'MESH':
            self.report({'ERROR_INVALID_CONTEXT'}, "Must select Mesh object")
            return {'CANCALLED'}

        args = (self, context)
        self._handle = bpy.types.SpaceView3D.draw_handler_add(self.draw_handler, args, 'WINDOW', 'POST_PIXEL')

        context.window_manager.modal_handler_add(self)
        # return {'RUNNING_MODAL'}
        return self.execute(context)

    
    def modal(self, context, event):
        context.area.header_text_set("Running modal")

        context.area.tag_redraw()
        
        if event.type == 'LEFTMOUSE':
            context.area.header_text_set()
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            context.area.header_text_set()
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}
        
        else:
            return {'PASS_THROUGH'}

        return {'RUNNING_MODAL'}


    def draw_handler(self, context, args):
        # Draw stuff here
        bgl.glEnable(bgl.GL_BLEND)
        bgl.glColor4f(1.0, 0.0, 1.0, 1.0)
        bgl.glPointSize(4)

        bgl.glBegin(bgl.GL_POINTS)
        for point in self.points:
            x, y = location_3d_to_region_2d(bpy.context.region, bpy.context.space_data.region_3d, point)
            bgl.glVertex2f(x, y)

        bgl.glEnd()

        # restore opengl defaults
        bgl.glPointSize(1)
        bgl.glDisable(bgl.GL_BLEND)
        bgl.glColor4f(0.0, 0.0, 0.0, 1.0)

    def execute(self, context):
        bvh = BVHTree.FromObject(context.object, context.scene)

        # Get object data
        # TODO: Make these into properties stored external to the operator
        camera = bpy.data.objects['Camera']

        # Find out which direction the camera is pointing
        # TODO: Modify to cast a grid of vectors using camera.data.angle_x/y
        ray_dir = Vector((0, 0, -1))
        ray_dir.rotate(camera.rotation_euler)

        # Cast a ray towards the center of the camera view
        loc, norm, index, distance = bvh.ray_cast(camera.location, ray_dir)
        if loc is not None:
            self.points.append(loc)
        print(loc)

        return {'RUNNING_MODAL'}
