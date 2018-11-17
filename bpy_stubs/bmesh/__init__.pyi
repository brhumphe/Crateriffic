from typing import Any
import bpy


# TODO: Create modules for this later
#BMesh = ... # type: Any

def from_edit_mesh(mesh: bpy.types.Mesh) -> BMesh:
    """
   Return a BMesh from this mesh, currently the mesh must already be in editmode.

   :arg mesh: The editmode mesh.
   :type mesh: bpy.types.mesh.pyi
   :return: the BMesh associated with this mesh.
   :rtype: bmesh.types.bmesh.pyi
   """
    ...


def update_edit_mesh(mesh: bpy.types.Mesh, tessface=True, destructive=True) -> None:
    """
    Update the mesh after changes to the BMesh in editmode,
    optionally recalculating n-gon tessellation.

    :arg mesh: The editmode mesh.
    :type mesh: :class:`bpy.types.Mesh`
    :arg tessface: Option to recalculate n-gon tessellation.
    :type tessface: boolean
    :arg destructive: Use when geometry has been added or removed.
    :type destructive: boolean
    """