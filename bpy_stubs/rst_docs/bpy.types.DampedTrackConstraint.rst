DampedTrackConstraint(Constraint)
=================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: DampedTrackConstraint(Constraint)

   Point toward target by taking the shortest rotation path

   .. attribute:: head_tail

      Target along length of bone: Head=0, Tail=1

      :type: float in [0, 1], default 0.0

   .. attribute:: subtarget

      :type: string, default "", (never None)

   .. attribute:: target

      Target Object

      :type: :class:`Object`

   .. attribute:: track_axis

      Axis that points to the target object

      :type: enum in ['TRACK_X', 'TRACK_Y', 'TRACK_Z', 'TRACK_NEGATIVE_X', 'TRACK_NEGATIVE_Y', 'TRACK_NEGATIVE_Z'], default 'TRACK_X'

   .. attribute:: use_bbone_shape

      Follow shape of B-Bone segments when calculating Head/Tail position

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

