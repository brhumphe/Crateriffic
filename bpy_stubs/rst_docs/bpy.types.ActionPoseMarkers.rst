ActionPoseMarkers(bpy_struct)
=============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ActionPoseMarkers(bpy_struct)

   Collection of timeline markers

   .. attribute:: active

      Active pose marker for this action

      :type: :class:`TimelineMarker`

   .. attribute:: active_index

      Index of active pose marker

      :type: int in [0, inf], default 0

   .. method:: new(name)

      Add a pose marker to the action

      :arg name:

         New name for the marker (not unique)

      :type name: string, (never None)
      :return:

         Newly created marker

      :rtype: :class:`TimelineMarker`

   .. method:: remove(marker)

      Remove a timeline marker

      :arg marker:

         Timeline marker to remove

      :type marker: :class:`TimelineMarker`, (never None)

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

   * :class:`Action.pose_markers`

