Linesets(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Linesets(bpy_struct)

   Line sets for associating lines and style parameters

   .. data:: active

      Active line set being displayed

      :type: :class:`FreestyleLineSet`, (readonly)

   .. attribute:: active_index

      Index of active line set slot

      :type: int in [0, inf], default 0

   .. method:: new(name)

      Add a line set to scene render layer Freestyle settings

      :arg name:

         New name for the line set (not unique)

      :type name: string, (never None)
      :return:

         Newly created line set

      :rtype: :class:`FreestyleLineSet`

   .. method:: remove(lineset)

      Remove a line set from scene render layer Freestyle settings

      :arg lineset:

         Line set to remove

      :type lineset: :class:`FreestyleLineSet`, (never None)

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

   * :class:`FreestyleSettings.linesets`

