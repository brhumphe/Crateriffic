LineStyleThicknessModifiers(bpy_struct)
=======================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: LineStyleThicknessModifiers(bpy_struct)

   Thickness modifiers for changing line thickness

   .. method:: new(name, type)

      Add a thickness modifier to line style

      :arg name:

         New name for the thickness modifier (not unique)

      :type name: string, (never None)
      :arg type:

         Thickness modifier type to add

      :type type: enum in ['ALONG_STROKE', 'CALLIGRAPHY', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT']
      :return:

         Newly added thickness modifier

      :rtype: :class:`LineStyleThicknessModifier`

   .. method:: remove(modifier)

      Remove a thickness modifier from line style

      :arg modifier:

         Thickness modifier to remove

      :type modifier: :class:`LineStyleThicknessModifier`, (never None)

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

   * :class:`FreestyleLineStyle.thickness_modifiers`

