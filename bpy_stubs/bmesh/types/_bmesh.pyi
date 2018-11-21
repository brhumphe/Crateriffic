import bpy

__all__ = ['BMesh']

class BMesh:

    def from_mesh(self, mesh: bpy.types.Mesh, face_normals=True, shape_key_index=0) -> BMesh:
        """
        Initialize this bmesh from existing mesh datablock.
        :param mesh: The mesh data to load.
        :param face_normals: Use the locations from a shape key.
        :param shape_key_index: The shape key index to use.
        :return:
        """
