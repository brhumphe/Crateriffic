from typing import Set

import bpy
from bpy.types import bpy_struct


class Operator(bpy_struct):
    """
    Storage of an operator being executed, or registered after execution
    """

    bl_description = ...  # type: str
    bl_idname = ...  # type: str
    bl_label = ...  # type: str
    bl_options = ...  # type: Set[str]
    bl_translation_context = ...  # type: str
    bl_undo_group = ...  # type: str
    has_reports = ...  # type: bool
    layout = ...  # type: UILayout
    macros = ...  # type: bpy_prop_collection[Macro]
    name = ...  # type: str
    options = ...  # type: OperatorOptions
    properties = ...  # type: OperatorProperties
    bl_property = ...  # type: str

    def report(self, report_type: Set[str], message: str):
        """
        report
        :param message: Report message
        :type report_type: enum set in {'DEBUG', 'INFO', 'OPERATOR', 'PROPERTY', 'WARNING', 'ERROR', 'ERROR_INVALID_INPUT', 'ERROR_INVALID_CONTEXT', 'ERROR_OUT_OF_MEMORY'}
        """
        ...

    def is_repeat(self) -> bool:
        ...

    @classmethod
    def poll(cls, context: bpy.context) -> bool:
        """Test if the operator can be called or not"""
        ...

    def execute(self, context: bpy.context) -> Set[str]:
        """Execute the operator"""
        ...
