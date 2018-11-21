AnimViz(bpy_struct)
===================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AnimViz(bpy_struct)

   Settings for the visualization of motion

   .. data:: motion_path

      Motion Path settings for visualization

      :type: :class:`AnimVizMotionPaths`, (readonly, never None)

   .. data:: onion_skin_frames

      Onion Skinning (ghosting) settings for visualization

      :type: :class:`AnimVizOnionSkinning`, (readonly, never None)

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

   * :class:`Object.animation_visualization`
   * :class:`Pose.animation_visualization`

