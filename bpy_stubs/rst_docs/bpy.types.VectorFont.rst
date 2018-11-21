VectorFont(ID)
==============

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: VectorFont(ID)

   Vector font for Text objects

   .. attribute:: filepath

      :type: string, default "", (never None)

   .. data:: packed_file

      :type: :class:`PackedFile`, (readonly)

   .. method:: pack()

      Pack the font into the current blend file


   .. method:: unpack(method='USE_LOCAL')

      Unpack the font to the samples filename

      :arg method:

         method, How to unpack

      :type method: enum in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL'], (optional)

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

.. rubric:: References

.. hlist::
   :columns: 2

   * :class:`BlendData.fonts`
   * :class:`BlendDataFonts.load`
   * :class:`BlendDataFonts.remove`
   * :class:`TextCurve.font`
   * :class:`TextCurve.font_bold`
   * :class:`TextCurve.font_bold_italic`
   * :class:`TextCurve.font_italic`

