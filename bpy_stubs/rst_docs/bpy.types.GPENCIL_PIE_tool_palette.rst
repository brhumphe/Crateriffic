GPENCIL_PIE_tool_palette(Menu)
==============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Menu`

.. class:: GPENCIL_PIE_tool_palette(Menu)

   

   .. method:: draw(context)

   .. method:: draw_preset(context)

      Define these on the subclass:
      - preset_operator (string)
      - preset_subdir (string)
      
      Optionally:
      - preset_extensions (set of strings)
      - preset_operator_defaults (dict of keyword args)

   .. method:: path_menu(searchpaths, operator, *, props_default=None, prop_filepath='filepath', filter_ext=None, filter_path=None, display_name=None)

      Populate a menu from a list of paths.
      
      :arg searchpaths: Paths to scan.
      :type searchpaths: sequence of strings.
      :arg operator: The operator id to use with each file.
      :type operator: string
      :arg prop_filepath: Optional operator filepath property (defaults to "filepath").
      :type prop_filepath: string
      :arg props_default: Properties to assign to each operator.
      :type props_default: dict
      :arg filter_ext: Optional callback that takes the file extensions.
      
         Returning false excludes the file from the list.
      
      :type filter_ext: Callable that takes a string and returns a bool.
      :arg display_name: Optional callback that takes the full path, returns the name to display.
      :type display_name: Callable that takes a string and returns a string.

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Menu.layout`
   * :class:`Menu.bl_idname`
   * :class:`Menu.bl_label`
   * :class:`Menu.bl_translation_context`
   * :class:`Menu.bl_description`

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
   * :class:`Menu.poll`
   * :class:`Menu.draw`
   * :class:`Menu.append`
   * :class:`Menu.draw_collapsible`
   * :class:`Menu.draw_preset`
   * :class:`Menu.is_extended`
   * :class:`Menu.path_menu`
   * :class:`Menu.prepend`
   * :class:`Menu.remove`

