BoneGroups(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BoneGroups(bpy_struct)

   Collection of bone groups

   .. attribute:: active

      Active bone group for this pose

      :type: :class:`BoneGroup`

   .. attribute:: active_index

      Active index in bone groups array

      :type: int in [0, inf], default 0

   .. method:: new(name="Group")

      Add a new bone group to the object

      :arg name:

         Name of the new group

      :type name: string, (optional, never None)
      :return:

         New bone group

      :rtype: :class:`BoneGroup`

   .. method:: remove(group)

      Remove a bone group from this object

      :arg group:

         Removed bone group

      :type group: :class:`BoneGroup`, (never None)

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

   * :class:`Pose.bone_groups`

