CyclesDeviceSettings(PropertyGroup)
===================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`PropertyGroup`

.. class:: CyclesDeviceSettings(PropertyGroup)

   

   .. attribute:: id

      :type: string, default "", (never None)

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: type

      * ``CPU`` CPU, CPU.
      * ``CUDA`` CUDA, CUDA.
      * ``OPENCL`` OpenCL, OpenCL.

      :type: enum in ['CPU', 'CUDA', 'OPENCL'], default 'CUDA'

   .. attribute:: use

      :type: boolean, default True

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`PropertyGroup.name`

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

   * :class:`CyclesPreferences.devices`

