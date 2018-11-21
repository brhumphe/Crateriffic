IMAGE_UV_sculpt(Panel)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Panel`

.. class:: IMAGE_UV_sculpt(Panel)

   

   .. method:: draw(context)

   .. staticmethod:: paint_settings(context)

   .. staticmethod:: prop_unified_color(parent, context, brush, prop_name, text='')

   .. staticmethod:: prop_unified_color_picker(parent, context, brush, prop_name, value_slider=True)

   .. staticmethod:: prop_unified_size(parent, context, brush, prop_name, icon='NONE', text='', slider=False)

   .. staticmethod:: prop_unified_strength(parent, context, brush, prop_name, icon='NONE', text='', slider=False)

   .. staticmethod:: prop_unified_weight(parent, context, brush, prop_name, icon='NONE', text='', slider=False)

   .. staticmethod:: unified_paint_settings(parent, context)

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Panel.layout`
   * :class:`Panel.text`
   * :class:`Panel.bl_idname`
   * :class:`Panel.bl_label`
   * :class:`Panel.bl_translation_context`
   * :class:`Panel.bl_category`
   * :class:`Panel.bl_space_type`
   * :class:`Panel.bl_region_type`
   * :class:`Panel.bl_context`
   * :class:`Panel.bl_options`
   * :class:`Panel.use_pin`

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
   * :class:`Panel.poll`
   * :class:`Panel.draw`
   * :class:`Panel.draw_header`
   * :class:`Panel.append`
   * :class:`Panel.is_extended`
   * :class:`Panel.prepend`
   * :class:`Panel.remove`

