PackedFile(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PackedFile(bpy_struct)

   External file packed into the .blend file

   .. data:: data

      Raw data (bytes, exact content of the embedded file)

      :type: string, default "", (readonly, never None)

   .. data:: size

      Size of packed file in bytes

      :type: int in [-inf, inf], default 0, (readonly)

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

   * :class:`Image.packed_file`
   * :class:`ImagePackedFile.packed_file`
   * :class:`Library.packed_file`
   * :class:`Sound.packed_file`
   * :class:`VectorFont.packed_file`

