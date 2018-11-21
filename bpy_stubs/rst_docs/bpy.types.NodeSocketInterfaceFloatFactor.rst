NodeSocketInterfaceFloatFactor(NodeSocketInterfaceStandard)
===========================================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`NodeSocketInterface`, :class:`NodeSocketInterfaceStandard`

.. class:: NodeSocketInterfaceFloatFactor(NodeSocketInterfaceStandard)

   Floating point number socket of a node

   .. attribute:: default_value

      Input value used for unconnected socket

      :type: float in [0, 1], default 1.0

   .. attribute:: max_value

      Maximum value

      :type: float in [-inf, inf], default 0.0

   .. attribute:: min_value

      Minimum value

      :type: float in [-inf, inf], default 0.0

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`NodeSocketInterface.name`
   * :class:`NodeSocketInterface.identifier`
   * :class:`NodeSocketInterface.is_output`
   * :class:`NodeSocketInterface.bl_socket_idname`
   * :class:`NodeSocketInterfaceStandard.type`

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
   * :class:`NodeSocketInterface.draw`
   * :class:`NodeSocketInterface.draw_color`
   * :class:`NodeSocketInterface.register_properties`
   * :class:`NodeSocketInterface.init_socket`
   * :class:`NodeSocketInterface.from_socket`
   * :class:`NodeSocketInterfaceStandard.draw`
   * :class:`NodeSocketInterfaceStandard.draw_color`

