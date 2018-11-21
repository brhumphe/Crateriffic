GPencilPalette(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilPalette(bpy_struct)

   Collection of related palettes

   .. data:: colors

      Colors of the palette

      :type: :class:`GPencilPaletteColors` :class:`bpy_prop_collection` of :class:`GPencilPaletteColor`, (readonly)

   .. attribute:: name

      Palette name

      :type: string, default "", (never None)

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

   * :mod:`bpy.context.active_gpencil_palette`
   * :class:`GreasePencil.palettes`
   * :class:`GreasePencilPalettes.active`
   * :class:`GreasePencilPalettes.new`
   * :class:`GreasePencilPalettes.remove`

