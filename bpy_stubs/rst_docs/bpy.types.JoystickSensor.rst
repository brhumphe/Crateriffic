JoystickSensor(Sensor)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Sensor`

.. class:: JoystickSensor(Sensor)

   Sensor to detect joystick events

   .. attribute:: axis_direction

      The direction of the axis

      :type: enum in ['RIGHTAXIS', 'UPAXIS', 'LEFTAXIS', 'DOWNAXIS'], default 'RIGHTAXIS'

   .. attribute:: axis_number

      Which axis pair to use, 1 is usually the main direction input

      :type: int in [1, 8], default 0

   .. attribute:: axis_threshold

      Precision of the axis

      :type: int in [0, 32768], default 0

   .. attribute:: button_number

      Which button to use

      :type: int in [0, 18], default 0

   .. attribute:: event_type

      The type of event this joystick sensor is triggered on

      :type: enum in ['BUTTON', 'AXIS', 'HAT', 'AXIS_SINGLE'], default 'BUTTON'

   .. attribute:: hat_direction

      Hat direction

      :type: enum in ['UP', 'DOWN', 'LEFT', 'RIGHT', 'UPRIGHT', 'DOWNLEFT', 'UPLEFT', 'DOWNRIGHT'], default 'UP'

   .. attribute:: hat_number

      Which hat to use

      :type: int in [1, 2], default 0

   .. attribute:: joystick_index

      Which joystick to use

      :type: int in [0, 7], default 0

   .. attribute:: single_axis_number

      Single axis (vertical/horizontal/other) to detect

      :type: int in [1, 16], default 0

   .. attribute:: use_all_events

      Triggered by all events on this joystick's current type (axis/button/hat)

      :type: boolean, default False

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

