CompositorNodeColorBalance(CompositorNode)
==========================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`CompositorNode`

.. class:: CompositorNodeColorBalance(CompositorNode)

   

   .. attribute:: correction_method

      * ``LIFT_GAMMA_GAIN`` Lift/Gamma/Gain.
      * ``OFFSET_POWER_SLOPE`` Offset/Power/Slope (ASC-CDL), ASC-CDL standard color correction.

      :type: enum in ['LIFT_GAMMA_GAIN', 'OFFSET_POWER_SLOPE'], default 'LIFT_GAMMA_GAIN'

   .. attribute:: gain

      Correction for Highlights

      :type: float array of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. attribute:: gamma

      Correction for Midtones

      :type: float array of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. attribute:: lift

      Correction for Shadows

      :type: float array of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. attribute:: offset

      Correction for Shadows

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: offset_basis

      Support negative color by using this as the RGB basis

      :type: float in [-inf, inf], default 0.0

   .. attribute:: power

      Correction for Midtones

      :type: float array of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. attribute:: slope

      Correction for Highlights

      :type: float array of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. classmethod:: is_registered_node_type()

      True if a registered node type

      :return:

         Result

      :rtype: boolean

   .. classmethod:: input_template(index)

      Input socket template

      :arg index:

         Index

      :type index: int in [0, inf]
      :return:

         result

      :rtype: :class:`NodeInternalSocketTemplate`

   .. classmethod:: output_template(index)

      Output socket template

      :arg index:

         Index

      :type index: int in [0, inf]
      :return:

         result

      :rtype: :class:`NodeInternalSocketTemplate`

   .. method:: update()

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Node.type`
   * :class:`Node.location`
   * :class:`Node.width`
   * :class:`Node.width_hidden`
   * :class:`Node.height`
   * :class:`Node.dimensions`
   * :class:`Node.name`
   * :class:`Node.label`
   * :class:`Node.inputs`
   * :class:`Node.outputs`
   * :class:`Node.internal_links`
   * :class:`Node.parent`
   * :class:`Node.use_custom_color`
   * :class:`Node.color`
   * :class:`Node.select`
   * :class:`Node.show_options`
   * :class:`Node.show_preview`
   * :class:`Node.hide`
   * :class:`Node.mute`
   * :class:`Node.show_texture`
   * :class:`Node.shading_compatibility`
   * :class:`Node.bl_idname`
   * :class:`Node.bl_label`
   * :class:`Node.bl_description`
   * :class:`Node.bl_icon`
   * :class:`Node.bl_static_type`
   * :class:`Node.bl_width_default`
   * :class:`Node.bl_width_min`
   * :class:`Node.bl_width_max`
   * :class:`Node.bl_height_default`
   * :class:`Node.bl_height_min`
   * :class:`Node.bl_height_max`

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
   * :class:`Node.socket_value_update`
   * :class:`Node.is_registered_node_type`
   * :class:`Node.poll`
   * :class:`Node.poll_instance`
   * :class:`Node.update`
   * :class:`Node.insert_link`
   * :class:`Node.init`
   * :class:`Node.copy`
   * :class:`Node.free`
   * :class:`Node.draw_buttons`
   * :class:`Node.draw_buttons_ext`
   * :class:`Node.draw_label`
   * :class:`Node.poll`
   * :class:`NodeInternal.poll`
   * :class:`NodeInternal.poll_instance`
   * :class:`NodeInternal.update`
   * :class:`NodeInternal.draw_buttons`
   * :class:`NodeInternal.draw_buttons_ext`
   * :class:`CompositorNode.tag_need_exec`
   * :class:`CompositorNode.poll`
   * :class:`CompositorNode.update`

