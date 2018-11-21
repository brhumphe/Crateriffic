ColorBalanceModifier(SequenceModifier)
======================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`SequenceModifier`

.. class:: ColorBalanceModifier(SequenceModifier)

   Color balance modifier for sequence strip

   .. data:: color_balance

      :type: :class:`SequenceColorBalanceData`, (readonly)

   .. attribute:: color_multiply

      Multiply the intensity of each pixel

      :type: float in [0, 20], default 1.0

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`SequenceModifier.name`
   * :class:`SequenceModifier.type`
   * :class:`SequenceModifier.mute`
   * :class:`SequenceModifier.show_expanded`
   * :class:`SequenceModifier.input_mask_type`
   * :class:`SequenceModifier.mask_time`
   * :class:`SequenceModifier.input_mask_strip`
   * :class:`SequenceModifier.input_mask_id`

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

