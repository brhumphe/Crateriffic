MaterialTextureSlots(bpy_struct)
================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaterialTextureSlots(bpy_struct)

   Collection of texture slots

   .. classmethod:: add()

      add

      :return:

         The newly initialized mtex

      :rtype: :class:`MaterialTextureSlot`

   .. classmethod:: create(index)

      create

      :arg index:

         Index, Slot index to initialize

      :type index: int in [0, inf]
      :return:

         The newly initialized mtex

      :rtype: :class:`MaterialTextureSlot`

   .. classmethod:: clear(index)

      clear

      :arg index:

         Index, Slot index to clear

      :type index: int in [0, inf]

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

   * :class:`Material.texture_slots`

