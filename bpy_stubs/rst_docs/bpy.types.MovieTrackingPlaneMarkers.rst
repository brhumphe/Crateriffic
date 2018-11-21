MovieTrackingPlaneMarkers(bpy_struct)
=====================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingPlaneMarkers(bpy_struct)

   Collection of markers for movie tracking plane track

   .. method:: find_frame(frame, exact=True)

      Get plane marker for specified frame

      :arg frame:

         Frame, Frame number to find marker for

      :type frame: int in [0, 1048574]
      :arg exact:

         Exact, Get plane marker at exact frame number rather than get estimated marker

      :type exact: boolean, (optional)
      :return:

         Plane marker for specified frame

      :rtype: :class:`MovieTrackingPlaneMarker`

   .. method:: insert_frame(frame)

      Insert a new plane marker at the specified frame

      :arg frame:

         Frame, Frame number to insert marker to

      :type frame: int in [0, 1048574]
      :return:

         Newly created plane marker

      :rtype: :class:`MovieTrackingPlaneMarker`

   .. method:: delete_frame(frame)

      Delete plane marker at specified frame

      :arg frame:

         Frame, Frame number to delete plane marker from

      :type frame: int in [0, 1048574]

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

   * :class:`MovieTrackingPlaneTrack.markers`

