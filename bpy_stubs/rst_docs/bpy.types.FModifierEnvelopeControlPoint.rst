FModifierEnvelopeControlPoint(bpy_struct)
=========================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FModifierEnvelopeControlPoint(bpy_struct)

   Control point for envelope F-Modifier

   .. attribute:: frame

      Frame this control-point occurs on

      :type: float in [-inf, inf], default 0.0

   .. attribute:: max

      Upper bound of envelope at this control-point

      :type: float in [-inf, inf], default 0.0

   .. attribute:: min

      Lower bound of envelope at this control-point

      :type: float in [-inf, inf], default 0.0

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

   * :class:`FModifierEnvelope.control_points`
   * :class:`FModifierEnvelopeControlPoints.add`
   * :class:`FModifierEnvelopeControlPoints.remove`

