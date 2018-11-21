LineStyleAlphaModifier(LineStyleModifier)
=========================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`LineStyleModifier`

subclasses --- 
:class:`LineStyleAlphaModifier_AlongStroke`, :class:`LineStyleAlphaModifier_CreaseAngle`, :class:`LineStyleAlphaModifier_Curvature_3D`, :class:`LineStyleAlphaModifier_DistanceFromCamera`, :class:`LineStyleAlphaModifier_DistanceFromObject`, :class:`LineStyleAlphaModifier_Material`, :class:`LineStyleAlphaModifier_Noise`, :class:`LineStyleAlphaModifier_Tangent`

.. class:: LineStyleAlphaModifier(LineStyleModifier)

   Base type to define alpha transparency modifiers

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`

.. rubric:: Inherited Functions

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`

.. rubric:: References

.. hlist::
   :columns: 2

   * :class:`FreestyleLineStyle.alpha_modifiers`
   * :class:`LineStyleAlphaModifiers.new`
   * :class:`LineStyleAlphaModifiers.remove`

