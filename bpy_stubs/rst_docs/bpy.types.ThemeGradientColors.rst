ThemeGradientColors(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeGradientColors(bpy_struct)

   Theme settings for background colors and gradient

   .. attribute:: gradient

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: high_gradient

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: show_grad

      Do a gradient for the background of the viewport working area

      :type: boolean, default False

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

   * :class:`ThemeSpaceGradient.gradients`

