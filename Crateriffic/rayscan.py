import bpy
import bmesh
from mathutils import Vector, bvhtree

class RayScanOperator(bpy.types.Operator):
    bl_idname = "mesh.rayscan"
    bl_label = "Ray Scan"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return context.object.type == 'MESH'


    def execute(self, context):
        print("Executing Ray Cast")

        return {'FINISHED'}


    def invoke(self, context, event):
        return self.execute(context)

    