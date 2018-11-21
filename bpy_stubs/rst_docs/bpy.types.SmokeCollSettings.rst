SmokeCollSettings(bpy_struct)
=============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SmokeCollSettings(bpy_struct)

   Smoke collision settings

   .. attribute:: collision_type

      Collision type

      * ``COLLSTATIC`` Static, Non moving obstacle.
      * ``COLLRIGID`` Rigid, Rigid obstacle.
      * ``COLLANIMATED`` Animated, Animated obstacle.

      :type: enum in ['COLLSTATIC', 'COLLRIGID', 'COLLANIMATED'], default 'COLLSTATIC'

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

   * :class:`SmokeModifier.coll_settings`

