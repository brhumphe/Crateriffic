GameSoftBodySettings(bpy_struct)
================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GameSoftBodySettings(bpy_struct)

   Soft body simulation settings for an object in the game engine

   .. attribute:: cluster_iterations

      Number of cluster iterations

      :type: int in [1, 128], default 0

   .. attribute:: collision_margin

      Collision margin for soft body. Small value makes the algorithm unstable

      :type: float in [0.01, 1], default 0.0

   .. attribute:: dynamic_friction

      Dynamic Friction

      :type: float in [0, 1], default 0.0

   .. attribute:: linear_stiffness

      Linear stiffness of the soft body links

      :type: float in [0, 1], default 0.0

   .. attribute:: location_iterations

      Position solver iterations

      :type: int in [0, 10], default 0

   .. attribute:: shape_threshold

      Shape matching threshold

      :type: float in [0, 1], default 0.0

   .. attribute:: use_bending_constraints

      Enable bending constraints

      :type: boolean, default False

   .. attribute:: use_cluster_rigid_to_softbody

      Enable cluster collision between soft and rigid body

      :type: boolean, default False

   .. attribute:: use_cluster_soft_to_softbody

      Enable cluster collision between soft and soft body

      :type: boolean, default False

   .. attribute:: use_shape_match

      Enable soft body shape matching goal

      :type: boolean, default False

   .. attribute:: weld_threshold

      Welding threshold: distance between nearby vertices to be considered equal => set to 0.0 to disable welding test and speed up scene loading (ok if the mesh has no duplicates)

      :type: float in [0, 0.01], default 0.0

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

   * :class:`GameObjectSettings.soft_body`

