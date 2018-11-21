FollowTrackConstraint(Constraint)
=================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: FollowTrackConstraint(Constraint)

   Lock motion to the target motion track

   .. attribute:: camera

      Camera to which motion is parented (if empty active scene camera is used)

      :type: :class:`Object`

   .. attribute:: clip

      Movie Clip to get tracking data from

      :type: :class:`MovieClip`

   .. attribute:: depth_object

      Object used to define depth in camera space by projecting onto surface of this object

      :type: :class:`Object`

   .. attribute:: frame_method

      How the footage fits in the camera frame

      :type: enum in ['STRETCH', 'FIT', 'CROP'], default 'STRETCH'

   .. attribute:: object

      Movie tracking object to follow (if empty, camera object is used)

      :type: string, default "", (never None)

   .. attribute:: track

      Movie tracking track to follow

      :type: string, default "", (never None)

   .. attribute:: use_3d_position

      Use 3D position of track to parent to

      :type: boolean, default False

   .. attribute:: use_active_clip

      Use active clip defined in scene

      :type: boolean, default False

   .. attribute:: use_undistorted_position

      Parent to undistorted position of 2D track

      :type: boolean, default False

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Constraint.name`
   * :class:`Constraint.type`
   * :class:`Constraint.owner_space`
   * :class:`Constraint.target_space`
   * :class:`Constraint.mute`
   * :class:`Constraint.show_expanded`
   * :class:`Constraint.is_valid`
   * :class:`Constraint.active`
   * :class:`Constraint.is_proxy_local`
   * :class:`Constraint.influence`
   * :class:`Constraint.error_location`
   * :class:`Constraint.error_rotation`

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

