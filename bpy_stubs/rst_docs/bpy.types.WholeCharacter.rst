WholeCharacter(KeyingSetInfo)
=============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`KeyingSetInfo`

.. class:: WholeCharacter(KeyingSetInfo)

   

   .. staticmethod:: addProp(ksi, ks, bone, prop, index=-1, use_groups=True)

   .. staticmethod:: doBBone(ksi, context, ks, pchan)

   .. staticmethod:: doCustomProps(ksi, ks, bone)

   .. staticmethod:: doLoc(ksi, ks, bone)

   .. staticmethod:: doRot3d(ksi, ks, bone)

   .. staticmethod:: doRot4d(ksi, ks, bone)

   .. staticmethod:: doScale(ksi, ks, bone)

   .. staticmethod:: generate(ksi, context, ks, bone)

   .. staticmethod:: iterator(ksi, context, ks)

   .. staticmethod:: poll(ksi, context)

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`KeyingSetInfo.bl_idname`
   * :class:`KeyingSetInfo.bl_label`
   * :class:`KeyingSetInfo.bl_description`
   * :class:`KeyingSetInfo.bl_options`

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
   * :class:`KeyingSetInfo.poll`
   * :class:`KeyingSetInfo.iterator`
   * :class:`KeyingSetInfo.generate`

