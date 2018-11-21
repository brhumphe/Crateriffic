ThemeSpaceGeneric(bpy_struct)
=============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeSpaceGeneric(bpy_struct)

   

   .. attribute:: back

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: button

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: button_text

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: button_text_hi

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: button_title

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: header

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: header_text

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: header_text_hi

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. data:: panelcolors

      :type: :class:`ThemePanelColors`, (readonly, never None)

   .. attribute:: tab_active

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: tab_back

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: tab_inactive

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: tab_outline

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: text

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: text_hi

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: title

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

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

   * :class:`ThemeClipEditor.space`
   * :class:`ThemeConsole.space`
   * :class:`ThemeDopeSheet.space`
   * :class:`ThemeFileBrowser.space`
   * :class:`ThemeGraphEditor.space`
   * :class:`ThemeImageEditor.space`
   * :class:`ThemeInfo.space`
   * :class:`ThemeLogicEditor.space`
   * :class:`ThemeNLAEditor.space`
   * :class:`ThemeNodeEditor.space`
   * :class:`ThemeOutliner.space`
   * :class:`ThemeProperties.space`
   * :class:`ThemeSequenceEditor.space`
   * :class:`ThemeTextEditor.space`
   * :class:`ThemeTimeline.space`
   * :class:`ThemeUserPreferences.space`

