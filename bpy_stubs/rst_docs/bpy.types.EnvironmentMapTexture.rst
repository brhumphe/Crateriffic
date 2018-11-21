EnvironmentMapTexture(Texture)
==============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`Texture`

.. class:: EnvironmentMapTexture(Texture)

   Environment map texture

   .. data:: environment_map

      Get the environment map associated with this texture

      :type: :class:`EnvironmentMap`, (readonly)

   .. attribute:: filter_eccentricity

      Maximum eccentricity (higher gives less blur at distant/oblique angles, but is also slower)

      :type: int in [1, 256], default 0

   .. attribute:: filter_probes

      Maximum number of samples (higher gives less blur at distant/oblique angles, but is also slower)

      :type: int in [1, 256], default 0

   .. attribute:: filter_size

      Multiply the filter size used by MIP Map and Interpolation

      :type: float in [0.1, 50], default 0.0

   .. attribute:: filter_type

      Texture filter to use for sampling image

      :type: enum in ['BOX', 'EWA', 'FELINE', 'AREA'], default 'BOX'

   .. attribute:: image

      Source image file to read the environment map from

      :type: :class:`Image`

   .. data:: image_user

      Parameters defining which layer, pass and frame of the image is displayed

      :type: :class:`ImageUser`, (readonly)

   .. attribute:: use_filter_size_min

      Use Filter Size as a minimal filter value in pixels

      :type: boolean, default False

   .. attribute:: use_mipmap

      Use auto-generated MIP maps for the image

      :type: boolean, default False

   .. attribute:: use_mipmap_gauss

      Use Gauss filter to sample down MIP maps

      :type: boolean, default False

   .. data:: users_material

      Materials that use this texture
      (readonly)

   .. data:: users_object_modifier

      Object modifiers that use this texture
      (readonly)

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
   * :class:`Texture.type`
   * :class:`Texture.use_clamp`
   * :class:`Texture.use_color_ramp`
   * :class:`Texture.color_ramp`
   * :class:`Texture.intensity`
   * :class:`Texture.contrast`
   * :class:`Texture.saturation`
   * :class:`Texture.factor_red`
   * :class:`Texture.factor_green`
   * :class:`Texture.factor_blue`
   * :class:`Texture.use_preview_alpha`
   * :class:`Texture.use_nodes`
   * :class:`Texture.node_tree`
   * :class:`Texture.animation_data`
   * :class:`Texture.users_material`
   * :class:`Texture.users_object_modifier`
   * :class:`Texture.users_material`
   * :class:`Texture.users_object_modifier`

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
   * :class:`Texture.evaluate`

