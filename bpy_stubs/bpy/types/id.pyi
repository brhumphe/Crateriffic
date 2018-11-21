from . import bpy_struct

__all__ = ['ID']


class ID(bpy_struct):
    """
    Base type for data-blocks, defining a unique name, linking from other libraries and garbage collection.
    """
    name = ''  # type: str
