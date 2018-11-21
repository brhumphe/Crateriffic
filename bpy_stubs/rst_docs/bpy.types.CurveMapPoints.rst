CurveMapPoints(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CurveMapPoints(bpy_struct)

   Collection of Curve Map Points

   .. method:: new(position, value)

      Add point to CurveMap

      :arg position:

         Position, Position to add point

      :type position: float in [-inf, inf]
      :arg value:

         Value, Value of point

      :type value: float in [-inf, inf]
      :return:

         New point

      :rtype: :class:`CurveMapPoint`

   .. method:: remove(point)

      Delete point from CurveMap

      :arg point:

         PointElement to remove

      :type point: :class:`CurveMapPoint`, (never None)

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

   * :class:`CurveMap.points`

