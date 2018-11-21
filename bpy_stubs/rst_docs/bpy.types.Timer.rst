Timer(bpy_struct)
=================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Timer(bpy_struct)

   Window event timer

   .. data:: time_delta

      Time since last step in seconds

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. data:: time_duration

      Time since last step in seconds

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. data:: time_step

      :type: float in [-inf, inf], default 0.0, (readonly)

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

   * :class:`WindowManager.event_timer_add`
   * :class:`WindowManager.event_timer_remove`

