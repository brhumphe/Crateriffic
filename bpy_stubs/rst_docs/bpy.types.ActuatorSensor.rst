ActuatorSensor(Sensor)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Sensor`

.. class:: ActuatorSensor(Sensor)

   Sensor to detect state modifications of actuators

   .. attribute:: actuator

      Actuator name, actuator active state modifications will be detected

      :type: string, default "", (never None)

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Sensor.name`
   * :class:`Sensor.type`
   * :class:`Sensor.pin`
   * :class:`Sensor.active`
   * :class:`Sensor.show_expanded`
   * :class:`Sensor.invert`
   * :class:`Sensor.use_level`
   * :class:`Sensor.use_pulse_true_level`
   * :class:`Sensor.use_pulse_false_level`
   * :class:`Sensor.tick_skip`
   * :class:`Sensor.use_tap`
   * :class:`Sensor.controllers`

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
   * :class:`Sensor.link`
   * :class:`Sensor.unlink`

