ColorRampElement(bpy_struct)
============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ColorRampElement(bpy_struct)

   Element defining a color at a position in the color ramp

   .. attribute:: alpha

      Set alpha of selected color stop

      :type: float in [0, inf], default 0.0

   .. attribute:: color

      Set color of selected color stop

      :type: float array of 4 items in [0, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: position

      Set position of selected color stop

      :type: float in [0, 1], default 0.0

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

   * :class:`ColorRamp.elements`
   * :class:`ColorRampElements.new`
   * :class:`ColorRampElements.remove`

