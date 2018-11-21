FModifierEnvelopeControlPoints(bpy_struct)
==========================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FModifierEnvelopeControlPoints(bpy_struct)

   Control points defining the shape of the envelope

   .. method:: add(frame)

      Add a control point to a FModifierEnvelope

      :arg frame:

         Frame to add this control-point

      :type frame: float in [-inf, inf]
      :return:

         Newly created control-point

      :rtype: :class:`FModifierEnvelopeControlPoint`

   .. method:: remove(point)

      Remove a control-point from an FModifierEnvelope

      :arg point:

         Control-point to remove

      :type point: :class:`FModifierEnvelopeControlPoint`, (never None)

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

