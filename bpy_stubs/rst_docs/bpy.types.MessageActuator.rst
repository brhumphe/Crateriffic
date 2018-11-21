MessageActuator(Actuator)
=========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: MessageActuator(Actuator)

   

   .. attribute:: body_message

      Optional, message body Text

      :type: string, default "", (never None)

   .. attribute:: body_property

      The message body will be set by the Property Value

      :type: string, default "", (never None)

   .. attribute:: body_type

      Toggle message type: either Text or a PropertyName

      :type: enum in ['TEXT', 'PROPERTY'], default 'TEXT'

   .. attribute:: subject

      Optional, message subject (this is what can be filtered on)

      :type: string, default "", (never None)

   .. attribute:: to_property

      Optional, send message to objects with this name only, or empty to broadcast

      :type: string, default "", (never None)

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Actuator.name`
   * :class:`Actuator.type`
   * :class:`Actuator.pin`
   * :class:`Actuator.show_expanded`
   * :class:`Actuator.active`

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
   * :class:`Actuator.link`
   * :class:`Actuator.unlink`

