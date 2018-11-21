from typing import Optional

from bpy.types.id import ID

__all__ = ['bpy_struct']

class bpy_struct:
    """
    Base class for all classes in bpy.types
    """
    id_data = Optional[ID]