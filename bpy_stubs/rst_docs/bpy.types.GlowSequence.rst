GlowSequence(EffectSequence)
============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Sequence`, :class:`EffectSequence`

.. class:: GlowSequence(EffectSequence)

   Sequence strip creating a glow effect

   .. attribute:: blur_radius

      Radius of glow effect

      :type: float in [0.5, 20], default 0.0

   .. attribute:: boost_factor

      Brightness multiplier

      :type: float in [0, 10], default 0.0

   .. attribute:: clamp

      Brightness limit of intensity

      :type: float in [0, 1], default 0.0

   .. attribute:: input_1

      First input for the effect strip

      :type: :class:`Sequence`, (never None)

   .. data:: input_count

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: quality

      Accuracy of the blur effect

      :type: int in [1, 5], default 0

   .. attribute:: threshold

      Minimum intensity to trigger a glow

      :type: float in [0, 1], default 0.0

   .. attribute:: use_only_boost

      Show the glow buffer only

      :type: boolean, default False

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Sequence.name`
   * :class:`Sequence.type`
   * :class:`Sequence.select`
   * :class:`Sequence.select_left_handle`
   * :class:`Sequence.select_right_handle`
   * :class:`Sequence.mute`
   * :class:`Sequence.lock`
   * :class:`Sequence.frame_final_duration`
   * :class:`Sequence.frame_duration`
   * :class:`Sequence.frame_start`
   * :class:`Sequence.frame_final_start`
   * :class:`Sequence.frame_final_end`
   * :class:`Sequence.frame_offset_start`
   * :class:`Sequence.frame_offset_end`
   * :class:`Sequence.frame_still_start`
   * :class:`Sequence.frame_still_end`
   * :class:`Sequence.channel`
   * :class:`Sequence.use_linear_modifiers`
   * :class:`Sequence.blend_type`
   * :class:`Sequence.blend_alpha`
   * :class:`Sequence.effect_fader`
   * :class:`Sequence.use_default_fade`
   * :class:`Sequence.speed_factor`
   * :class:`Sequence.modifiers`
   * :class:`EffectSequence.use_deinterlace`
   * :class:`EffectSequence.alpha_mode`
   * :class:`EffectSequence.use_flip_x`
   * :class:`EffectSequence.use_flip_y`
   * :class:`EffectSequence.use_float`
   * :class:`EffectSequence.use_reverse_frames`
   * :class:`EffectSequence.color_multiply`
   * :class:`EffectSequence.color_saturation`
   * :class:`EffectSequence.strobe`
   * :class:`EffectSequence.use_translation`
   * :class:`EffectSequence.transform`
   * :class:`EffectSequence.use_crop`
   * :class:`EffectSequence.crop`
   * :class:`EffectSequence.use_proxy`
   * :class:`EffectSequence.proxy`

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
   * :class:`Sequence.update`
   * :class:`Sequence.strip_elem_from_frame`
   * :class:`Sequence.swap`

