GPUFXSettings(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPUFXSettings(bpy_struct)

   Settings for GPU based compositing

   .. data:: dof

      :type: :class:`GPUDOFSettings`, (readonly, never None)

   .. data:: ssao

      :type: :class:`GPUSSAOSettings`, (readonly, never None)

   .. attribute:: use_dof

      Use depth of field on viewport using the values from active camera

      :type: boolean, default False

   .. attribute:: use_ssao

      Use screen space ambient occlusion of field on viewport

      :type: boolean, default False

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

   * :class:`SpaceView3D.fx_settings`

