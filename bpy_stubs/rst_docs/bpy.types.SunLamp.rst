SunLamp(Lamp)
=============

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`Lamp`

.. class:: SunLamp(Lamp)

   Constant direction parallel ray lamp

   .. attribute:: compression_threshold

      Deep shadow map compression threshold

      :type: float in [0, 1], default 0.0

   .. attribute:: ge_shadow_buffer_type

      The shadow mapping algorithm used

      * ``SIMPLE`` Simple, Simple shadow maps.
      * ``VARIANCE`` Variance, Variance shadow maps.

      :type: enum in ['SIMPLE', 'VARIANCE'], default 'SIMPLE'

   .. attribute:: shadow_adaptive_threshold

      Threshold for Adaptive Sampling (Raytraced shadows)

      :type: float in [0, 1], default 0.0

   .. attribute:: shadow_buffer_bias

      Shadow buffer sampling bias

      :type: float in [0.001, 5], default 0.0

   .. attribute:: shadow_buffer_bleed_bias

      Bias for reducing light-bleed on variance shadow maps

      :type: float in [0, 1], default 0.0

   .. attribute:: shadow_buffer_clip_end

      Shadow map clip end, beyond which objects will not generate shadows

      :type: float in [0, 9999], default 0.0

   .. attribute:: shadow_buffer_clip_start

      Shadow map clip start, below which objects will not generate shadows

      :type: float in [0, 9999], default 0.0

   .. attribute:: shadow_buffer_samples

      Number of shadow buffer samples

      :type: int in [1, 16], default 0

   .. attribute:: shadow_buffer_size

      Resolution of the shadow buffer, higher values give crisper shadows but use more memory

      :type: int in [128, 10240], default 0

   .. attribute:: shadow_buffer_soft

      Size of shadow buffer sampling area

      :type: float in [0, 100], default 0.0

   .. attribute:: shadow_buffer_type

      Type of shadow buffer

      * ``REGULAR`` Classical, Classic shadow buffer.
      * ``HALFWAY`` Classic-Halfway, Regular buffer, averaging the closest and 2nd closest Z value to reducing bias artifacts.
      * ``IRREGULAR`` Irregular, Irregular buffer produces sharp shadow always, but it doesn't show up for raytracing.
      * ``DEEP`` Deep, Deep shadow buffer supports transparency and better filtering, at the cost of more memory usage and processing time.

      :type: enum in ['REGULAR', 'HALFWAY', 'IRREGULAR', 'DEEP'], default 'REGULAR'

   .. attribute:: shadow_color

      Color of shadows cast by the lamp

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: shadow_filter_type

      Type of shadow filter (Buffer Shadows)

      * ``BOX`` Box, Apply the Box filter to shadow buffer samples.
      * ``TENT`` Tent, Apply the Tent Filter to shadow buffer samples.
      * ``GAUSS`` Gauss, Apply the Gauss filter to shadow buffer samples.

      :type: enum in ['BOX', 'TENT', 'GAUSS'], default 'BOX'

   .. attribute:: shadow_frustum_size

      Size of the frustum used for creating the shadow map

      :type: float in [-inf, inf], default 0.0

   .. attribute:: shadow_method

      * ``NOSHADOW`` No Shadow.
      * ``RAY_SHADOW`` Ray Shadow, Use ray tracing for shadow.

      :type: enum in ['NOSHADOW', 'RAY_SHADOW'], default 'NOSHADOW'

   .. attribute:: shadow_ray_sample_method

      Method for generating shadow samples: Adaptive QMC is fastest, Constant QMC is less noisy but slower

      :type: enum in ['ADAPTIVE_QMC', 'CONSTANT_QMC'], default 'ADAPTIVE_QMC'

   .. attribute:: shadow_ray_samples

      Number of samples taken extra (samples x samples)

      :type: int in [1, 64], default 0

   .. attribute:: shadow_sample_buffers

      Number of shadow buffers to render for better AA, this increases memory usage

      * ``BUFFERS_1`` 1, Only one buffer rendered.
      * ``BUFFERS_4`` 4, Render 4 buffers for better AA, this quadruples memory usage.
      * ``BUFFERS_9`` 9, Render 9 buffers for better AA, this uses nine times more memory.

      :type: enum in ['BUFFERS_1', 'BUFFERS_4', 'BUFFERS_9'], default 'BUFFERS_1'

   .. attribute:: shadow_soft_size

      Light size for ray shadow sampling (Raytraced shadows)

      :type: float in [0, inf], default 0.0

   .. attribute:: show_shadow_box

      Draw a box in 3D view to visualize which objects are contained in it

      :type: boolean, default False

   .. data:: sky

      Sky related settings for sun lamps

      :type: :class:`LampSkySettings`, (readonly, never None)

   .. attribute:: use_auto_clip_end

      Automatic calculation of clipping-end, based on visible vertices

      :type: boolean, default False

   .. attribute:: use_auto_clip_start

      Automatic calculation of clipping-start, based on visible vertices

      :type: boolean, default False

   .. attribute:: use_only_shadow

      Cast shadows only, without illuminating objects

      :type: boolean, default False

   .. attribute:: use_shadow

      :type: boolean, default False

   .. attribute:: use_shadow_layer

      Objects on the same layers only cast shadows

      :type: boolean, default False

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`ID.name`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.tag`
   * :class:`ID.is_updated`
   * :class:`ID.is_updated_data`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.preview`
   * :class:`Lamp.type`
   * :class:`Lamp.distance`
   * :class:`Lamp.energy`
   * :class:`Lamp.color`
   * :class:`Lamp.use_own_layer`
   * :class:`Lamp.use_negative`
   * :class:`Lamp.use_specular`
   * :class:`Lamp.use_diffuse`
   * :class:`Lamp.node_tree`
   * :class:`Lamp.use_nodes`
   * :class:`Lamp.animation_data`
   * :class:`Lamp.texture_slots`
   * :class:`Lamp.active_texture`
   * :class:`Lamp.active_texture_index`
   * :class:`Lamp.cycles`

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
   * :class:`ID.copy`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`

