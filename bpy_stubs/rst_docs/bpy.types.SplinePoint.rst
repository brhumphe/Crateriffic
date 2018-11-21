SplinePoint(bpy_struct)
=======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SplinePoint(bpy_struct)

   Spline point without handles

   .. attribute:: co

      Point coordinates

      :type: float array of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: hide

      Visibility status

      :type: boolean, default False

   .. attribute:: radius

      Radius for beveling

      :type: float in [0, inf], default 0.0

   .. attribute:: select

      Selection status

      :type: boolean, default False

   .. attribute:: tilt

      Tilt in 3D View

      :type: float in [-376.991, 376.991], default 0.0

   .. attribute:: weight

      NURBS weight

      :type: float in [-inf, inf], default 0.0

   .. attribute:: weight_softbody

      Softbody goal weight

      :type: float in [0.01, 100], default 0.0

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

   * :class:`Spline.points`

