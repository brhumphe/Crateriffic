StateActuator(Actuator)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: StateActuator(Actuator)

   Actuator to handle states

   .. attribute:: operation

      Select the bit operation on object state mask

      :type: enum in ['SET', 'ADD', 'REMOVE', 'CHANGE'], default 'SET'

   .. attribute:: states

      :type: boolean array of 30 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

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

