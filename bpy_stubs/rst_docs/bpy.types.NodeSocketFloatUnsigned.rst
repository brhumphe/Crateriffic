NodeSocketFloatUnsigned(NodeSocketStandard)
===========================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`NodeSocket`, :class:`NodeSocketStandard`

.. class:: NodeSocketFloatUnsigned(NodeSocketStandard)

   Floating point number socket of a node

   .. attribute:: default_value

      Input value used for unconnected socket

      :type: float in [0, inf], default 0.0

   .. data:: links

      List of node links from or to this socket
      (readonly)

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`NodeSocket.name`
   * :class:`NodeSocket.identifier`
   * :class:`NodeSocket.is_output`
   * :class:`NodeSocket.hide`
   * :class:`NodeSocket.enabled`
   * :class:`NodeSocket.link_limit`
   * :class:`NodeSocket.is_linked`
   * :class:`NodeSocket.show_expanded`
   * :class:`NodeSocket.hide_value`
   * :class:`NodeSocket.node`
   * :class:`NodeSocket.type`
   * :class:`NodeSocket.bl_idname`
   * :class:`NodeSocket.links`
   * :class:`NodeSocket.links`
   * :class:`NodeSocketStandard.links`
   * :class:`NodeSocketStandard.links`

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
   * :class:`NodeSocket.draw`
   * :class:`NodeSocket.draw_color`
   * :class:`NodeSocketStandard.draw`
   * :class:`NodeSocketStandard.draw_color`

