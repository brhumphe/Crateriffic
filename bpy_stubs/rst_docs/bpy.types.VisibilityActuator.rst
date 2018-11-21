VisibilityActuator(Actuator)
============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: VisibilityActuator(Actuator)

   Actuator to set visibility and occlusion of the object

   .. attribute:: apply_to_children

      Set all the children of this object to the same visibility/occlusion recursively

      :type: boolean, default False

   .. attribute:: use_occlusion

      Set the object to occlude objects behind it (initialized from the object type in physics button)

      :type: boolean, default False

   .. attribute:: use_visible

      Set the objects visible (initialized from the object render restriction toggle in physics button)

      :type: boolean, default False

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

