PaletteColors(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PaletteColors(bpy_struct)

   Collection of palette colors

   .. attribute:: active

      :type: :class:`PaletteColor`

   .. method:: new()

      Add a new color to the palette

      :return:

         The newly created color

      :rtype: :class:`PaletteColor`

   .. method:: remove(color)

      Remove a color from the palette

      :arg color:

         The color to remove

      :type color: :class:`PaletteColor`, (never None)

   .. method:: clear()

      Remove all colors from the palette


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

   * :class:`Palette.colors`

