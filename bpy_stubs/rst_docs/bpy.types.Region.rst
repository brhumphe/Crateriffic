Region(bpy_struct)
==================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Region(bpy_struct)

   Region in a subdivided screen area

   .. data:: height

      Region height

      :type: int in [0, 32767], default 0, (readonly)

   .. data:: id

      Unique ID for this region

      :type: int in [-32768, 32767], default 0, (readonly)

   .. data:: type

      Type of this region

      :type: enum in ['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'PREVIEW'], default 'WINDOW', (readonly)

   .. data:: view2d

      2D view of the region

      :type: :class:`View2D`, (readonly, never None)

   .. data:: width

      Region width

      :type: int in [0, 32767], default 0, (readonly)

   .. data:: x

      The window relative vertical location of the region

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: y

      The window relative horizontal location of the region

      :type: int in [-inf, inf], default 0, (readonly)

   .. method:: tag_redraw()

      tag_redraw


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

   * :class:`Area.regions`
   * :class:`Context.region`

