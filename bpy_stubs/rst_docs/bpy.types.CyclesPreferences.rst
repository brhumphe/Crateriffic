CyclesPreferences(AddonPreferences)
===================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`AddonPreferences`

.. class:: CyclesPreferences(AddonPreferences)

   

   .. attribute:: compute_device_type

      Device to use for computation (rendering with Cycles)

      :type: enum in [], default ''

   .. data:: devices

      :type: :class:`bpy_prop_collection` of :class:`CyclesDeviceSettings`, (readonly)

   .. method:: draw(context)

   .. method:: draw_impl(layout, context)

   .. method:: find_existing_device_entry(device)

   .. method:: get_device_types(context)

   .. method:: get_devices()

   .. method:: get_num_gpu_devices()

   .. method:: has_active_device()

   .. method:: update_device_entries(device_list)

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`AddonPreferences.bl_idname`

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

