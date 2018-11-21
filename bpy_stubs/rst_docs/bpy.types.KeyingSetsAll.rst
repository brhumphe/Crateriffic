KeyingSetsAll(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyingSetsAll(bpy_struct)

   All available keying sets

   .. attribute:: active

      Active Keying Set used to insert/delete keyframes

      :type: :class:`KeyingSet`

   .. attribute:: active_index

      Current Keying Set index (negative for 'builtin' and positive for 'absolute')

      :type: int in [-inf, inf], default 0

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

   * :class:`Scene.keying_sets_all`

