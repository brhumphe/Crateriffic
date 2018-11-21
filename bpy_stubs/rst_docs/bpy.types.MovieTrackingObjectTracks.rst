MovieTrackingObjectTracks(bpy_struct)
=====================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingObjectTracks(bpy_struct)

   Collection of movie tracking tracks

   .. attribute:: active

      Active track in this tracking data object

      :type: :class:`MovieTrackingTrack`

   .. method:: new(name="", frame=1)

      create new motion track in this movie clip

      :arg name:

         Name of new track

      :type name: string, (optional, never None)
      :arg frame:

         Frame, Frame number to add tracks on

      :type frame: int in [0, 1048574], (optional)
      :return:

         Newly created track

      :rtype: :class:`MovieTrackingTrack`

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

   * :class:`MovieTrackingObject.tracks`

