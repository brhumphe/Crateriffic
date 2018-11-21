ArmatureEditBones(bpy_struct)
=============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ArmatureEditBones(bpy_struct)

   Collection of armature edit bones

   .. attribute:: active

      Armatures active edit bone

      :type: :class:`EditBone`

   .. method:: new(name)

      Add a new bone

      :arg name:

         New name for the bone

      :type name: string, (never None)
      :return:

         Newly created edit bone

      :rtype: :class:`EditBone`

   .. method:: remove(bone)

      Remove an existing bone from the armature

      :arg bone:

         EditBone to remove

      :type bone: :class:`EditBone`, (never None)

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

   * :class:`Armature.edit_bones`

