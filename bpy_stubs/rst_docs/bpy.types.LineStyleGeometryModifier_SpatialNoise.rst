LineStyleGeometryModifier_SpatialNoise(LineStyleGeometryModifier)
=================================================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`LineStyleModifier`, :class:`LineStyleGeometryModifier`

.. class:: LineStyleGeometryModifier_SpatialNoise(LineStyleGeometryModifier)

   Add spatial noise to stroke backbone geometry

   .. attribute:: amplitude

      Amplitude of the spatial noise

      :type: float in [-inf, inf], default 0.0

   .. attribute:: expanded

      True if the modifier tab is expanded

      :type: boolean, default False

   .. attribute:: name

      Name of the modifier

      :type: string, default "", (never None)

   .. attribute:: octaves

      Number of octaves (i.e., the amount of detail of the spatial noise)

      :type: int in [0, inf], default 0

   .. attribute:: scale

      Scale of the spatial noise

      :type: float in [-inf, inf], default 0.0

   .. attribute:: smooth

      If true, the spatial noise is smooth

      :type: boolean, default False

   .. data:: type

      Type of the modifier

      :type: enum in ['2D_OFFSET', '2D_TRANSFORM', 'BACKBONE_STRETCHER', 'BEZIER_CURVE', 'BLUEPRINT', 'GUIDING_LINES', 'PERLIN_NOISE_1D', 'PERLIN_NOISE_2D', 'POLYGONIZATION', 'SAMPLING', 'SIMPLIFICATION', 'SINUS_DISPLACEMENT', 'SPATIAL_NOISE', 'TIP_REMOVER'], default '2D_OFFSET', (readonly)

   .. attribute:: use

      Enable or disable this modifier during stroke rendering

      :type: boolean, default False

   .. attribute:: use_pure_random

      If true, the spatial noise does not show any coherence

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

