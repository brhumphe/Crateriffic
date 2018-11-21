FileBrowserFSMenuEntry(bpy_struct)
==================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FileBrowserFSMenuEntry(bpy_struct)

   File Select Parameters

   .. data:: is_valid

      Whether this path is currently reachable

      :type: boolean, default False, (readonly)

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: path

      :type: string, default "", (never None)

   .. data:: use_save

      Whether this path is saved in bookmarks, or generated from OS

      :type: boolean, default False, (readonly)

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

   * :class:`SpaceFileBrowser.bookmarks`
   * :class:`SpaceFileBrowser.recent_folders`
   * :class:`SpaceFileBrowser.system_bookmarks`
   * :class:`SpaceFileBrowser.system_folders`

