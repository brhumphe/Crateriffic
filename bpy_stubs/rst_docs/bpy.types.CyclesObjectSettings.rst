CyclesObjectSettings(PropertyGroup)
===================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`PropertyGroup`

.. class:: CyclesObjectSettings(PropertyGroup)

   

   .. attribute:: dicing_rate

      Multiplier for scene dicing rate (located in the Geometry Panel)

      :type: float in [0.1, 1000], default 1.0

   .. attribute:: is_shadow_catcher

      Only render shadows on this object, for compositing renders into real footage

      :type: boolean, default False

   .. attribute:: motion_steps

      Control accuracy of deformation motion blur, more steps gives more memory usage (actual number of steps is 2^(steps - 1))

      :type: int in [1, inf], default 1

   .. attribute:: use_adaptive_subdivision

      Use adaptive render time subdivision

      :type: boolean, default False

   .. attribute:: use_camera_cull

      Allow this object and its duplicators to be culled by camera space culling

      :type: boolean, default False

   .. attribute:: use_deform_motion

      Use deformation motion blur for this object

      :type: boolean, default True

   .. attribute:: use_distance_cull

      Allow this object and its duplicators to be culled by distance from camera

      :type: boolean, default False

   .. attribute:: use_motion_blur

      Use motion blur for this object

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

   * :class:`Object.cycles`

