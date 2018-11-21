BoolProperty(Property)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Property`

.. class:: BoolProperty(Property)

   RNA boolean property definition

   .. data:: array_length

      Maximum length of the array, 0 means unlimited

      :type: int in [0, inf], default 0, (readonly)

   .. data:: default

      Default value for this number

      :type: boolean, default False, (readonly)

   .. data:: default_array

      Default value for this array

      :type: boolean array of 3 items, default (False, False, False), (readonly)

   .. data:: is_array

      :type: boolean, default False, (readonly)

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Property.name`
   * :class:`Property.identifier`
   * :class:`Property.description`
   * :class:`Property.translation_context`
   * :class:`Property.type`
   * :class:`Property.subtype`
   * :class:`Property.srna`
   * :class:`Property.unit`
   * :class:`Property.icon`
   * :class:`Property.is_readonly`
   * :class:`Property.is_animatable`
   * :class:`Property.is_required`
   * :class:`Property.is_argument_optional`
   * :class:`Property.is_never_none`
   * :class:`Property.is_hidden`
   * :class:`Property.is_skip_save`
   * :class:`Property.is_output`
   * :class:`Property.is_registered`
   * :class:`Property.is_registered_optional`
   * :class:`Property.is_runtime`
   * :class:`Property.is_enum_flag`
   * :class:`Property.is_library_editable`

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

