SmokeModifier(Modifier)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: SmokeModifier(Modifier)

   Smoke simulation modifier

   .. data:: coll_settings

      :type: :class:`SmokeCollSettings`, (readonly)

   .. data:: domain_settings

      :type: :class:`SmokeDomainSettings`, (readonly)

   .. data:: flow_settings

      :type: :class:`SmokeFlowSettings`, (readonly)

   .. attribute:: smoke_type

      * ``NONE`` None.
      * ``DOMAIN`` Domain.
      * ``FLOW`` Flow, Inflow/Outflow.
      * ``COLLISION`` Collision.

      :type: enum in ['NONE', 'DOMAIN', 'FLOW', 'COLLISION'], default 'NONE'

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.use_apply_on_spline`

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

