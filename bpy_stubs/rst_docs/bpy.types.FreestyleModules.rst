FreestyleModules(bpy_struct)
============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FreestyleModules(bpy_struct)

   A list of style modules (to be applied from top to bottom)

   .. method:: new()

      Add a style module to scene render layer Freestyle settings

      :return:

         Newly created style module

      :rtype: :class:`FreestyleModuleSettings`

   .. method:: remove(module)

      Remove a style module from scene render layer Freestyle settings

      :arg module:

         Style module to remove

      :type module: :class:`FreestyleModuleSettings`, (never None)

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

   * :class:`FreestyleSettings.modules`

