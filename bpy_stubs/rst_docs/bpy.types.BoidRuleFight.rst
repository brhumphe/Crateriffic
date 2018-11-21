BoidRuleFight(BoidRule)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`BoidRule`

.. class:: BoidRuleFight(BoidRule)

   

   .. attribute:: distance

      Attack boids at max this distance

      :type: float in [0, 100], default 0.0

   .. attribute:: flee_distance

      Flee to this distance

      :type: float in [0, 100], default 0.0

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`BoidRule.name`
   * :class:`BoidRule.type`
   * :class:`BoidRule.use_in_air`
   * :class:`BoidRule.use_on_land`

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

