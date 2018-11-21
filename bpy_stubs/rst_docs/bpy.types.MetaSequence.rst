MetaSequence(Sequence)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Sequence`

.. class:: MetaSequence(Sequence)

   Sequence strip to group other strips as a single sequence strip

   .. attribute:: alpha_mode

      Representation of alpha information in the RGBA pixels

      * ``STRAIGHT`` Straight, RGB channels in transparent pixels are unaffected by the alpha channel.
      * ``PREMUL`` Premultiplied, RGB channels in transparent pixels are multiplied by the alpha channel.

      :type: enum in ['STRAIGHT', 'PREMUL'], default 'STRAIGHT'

   .. attribute:: animation_offset_end

      Animation end offset (trim end)

      :type: int in [0, inf], default 0

   .. attribute:: animation_offset_start

      Animation start offset (trim start)

      :type: int in [0, inf], default 0

   .. attribute:: color_multiply

      :type: float in [0, 20], default 1.0

   .. attribute:: color_saturation

      Adjust the intensity of the input's color

      :type: float in [0, 20], default 1.0

   .. data:: crop

      :type: :class:`SequenceCrop`, (readonly)

   .. data:: proxy

      :type: :class:`SequenceProxy`, (readonly)

   .. data:: sequences

      :type: :class:`bpy_prop_collection` of :class:`Sequence`, (readonly)

   .. attribute:: strobe

      Only display every nth frame

      :type: float in [1, 30], default 0.0

   .. data:: transform

      :type: :class:`SequenceTransform`, (readonly)

   .. attribute:: use_crop

      Crop image before processing

      :type: boolean, default False

   .. attribute:: use_deinterlace

      Remove fields from video movies

      :type: boolean, default False

   .. attribute:: use_flip_x

      Flip on the X axis

      :type: boolean, default False

   .. attribute:: use_flip_y

      Flip on the Y axis

      :type: boolean, default False

   .. attribute:: use_float

      Convert input to float data

      :type: boolean, default False

   .. attribute:: use_proxy

      Use a preview proxy and/or timecode index for this strip

      :type: boolean, default False

   .. attribute:: use_reverse_frames

      Reverse frame order

      :type: boolean, default False

   .. attribute:: use_translation

      Translate image before processing

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

