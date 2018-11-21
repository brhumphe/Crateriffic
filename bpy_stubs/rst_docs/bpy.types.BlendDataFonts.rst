BlendDataFonts(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataFonts(bpy_struct)

   Collection of fonts

   .. data:: is_updated

      :type: boolean, default False, (readonly)

   .. method:: load(filepath, check_existing=False)

      Load a new font into the main database

      :arg filepath:

         path of the font to load

      :type filepath: string, (never None)
      :arg check_existing:

         Using existing data-block if this file is already loaded

      :type check_existing: boolean, (optional)
      :return:

         New font data-block

      :rtype: :class:`VectorFont`

   .. method:: remove(vfont, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a font from the current blendfile

      :arg vfont:

         Font to remove

      :type vfont: :class:`VectorFont`, (never None)
      :arg do_unlink:

         Unlink all usages of this font before deleting it

      :type do_unlink: boolean, (optional)
      :arg do_id_user:

         Decrement user counter of all datablocks used by this font

      :type do_id_user: boolean, (optional)
      :arg do_ui_user:

         Make sure interface does not reference this font

      :type do_ui_user: boolean, (optional)

   .. method:: tag(value)

      tag

      :arg value:

         Value

      :type value: boolean

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

   * :class:`BlendData.fonts`

