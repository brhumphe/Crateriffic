from typing import Optional, Union, List, Any, Tuple

from bpy.types import ID, FCurve

__all__ = ['bpy_struct']

class bpy_struct:
    """
    Base class for all classes in bpy.types
    """
    id_data = Optional[ID]

    def as_pointer(self) -> int:
        """
        Returns the memory address which holds a pointer to blenders internal data
        :return: int (memory address)
        """
        ...

    def driver_add(self, path: str, index: int = ...) -> Union[FCurve, List[FCurve]]:
        """
        Adds driver(s) to the given property
        :param path: path to the property to drive, analogous to the fcurve’s data path.
        :param index: array index of the property drive. Defaults to -1 for all indices or a single channel if the property is not an array.
        :return: The driver(s) added.
        """
        ...

    def driver_remove(self, path: str, index: int = ...) -> bool:
        """
        Remove driver(s) from the given property
        :param path: path to the property to drive, analogous to the fcurve’s data path.
        :param index: array index of the property drive. Defaults to -1 for all indices or a single channel if the property is not an array.
        :return: Success of driver removal.
        """

    def get(self, key, default=None) -> Any:
        """
        Returns the value of the custom property assigned to key or default when not found (matches pythons dictionary function of the same name).

        Note: Only bpy.types.ID, bpy.types.Bone and bpy.types.PoseBone classes support custom properties.
        :param key: The key associated with the custom property.
        :param default: Optional argument for the value to return if key is not found.
        :return: Value of custom property or default value
        """
        ...

    def is_property_hidden(self, prop: str) -> bool:
        """
        Check if a property is hidden.
        :param prop: Name of property
        :return:
        """
        ...

    def is_property_readonly(self, prop: str) -> bool:
        """
        Check if a property is readonly.
        :param prop: Name of property.
        :return:
        """
        ...

    def is_property_set(self, prop: str) -> bool:
        """
        Check if a property is set, use for testing operator properties.
        :param prop: Name of property.
        :return:
        """
        ...

    def items(self) -> List[Tuple[str, Any]]:
        """
        Returns the items of this objects custom properties (matches pythons dictionary function of the same name).
        :return: custom property key, value pairs.
        """
        ...
