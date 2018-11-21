NlaTracks(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: NlaTracks(bpy_struct)

   Collection of NLA Tracks

   .. attribute:: active

      Active Object constraint

      :type: :class:`NlaTrack`

   .. method:: new(prev=None)

      Add a new NLA Track

      :arg prev:

         NLA Track to add the new one after

      :type prev: :class:`NlaTrack`, (optional)
      :return:

         New NLA Track

      :rtype: :class:`NlaTrack`

   .. method:: remove(track)

      Remove a NLA Track

      :arg track:

         NLA Track to remove

      :type track: :class:`NlaTrack`, (never None)

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

   * :class:`AnimData.nla_tracks`

