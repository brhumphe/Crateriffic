SequenceElement(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SequenceElement(bpy_struct)

   Sequence strip data for a single frame

   .. attribute:: filename

      Name of the source file

      :type: string, default "", (never None)

   .. data:: orig_height

      Original image height

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: orig_width

      Original image width

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

   * :class:`ImageSequence.elements`
   * :class:`MovieSequence.elements`
   * :class:`Sequence.strip_elem_from_frame`
   * :class:`SequenceElements.append`

