MaterialPhysics(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaterialPhysics(bpy_struct)

   Physics settings for a Material data-block

   .. attribute:: elasticity

      Elasticity of collisions

      :type: float in [0, 1], default 0.0

   .. attribute:: fh_damping

      Damping of the spring force, when inside the physics distance area

      :type: float in [0, 1], default 0.0

   .. attribute:: fh_distance

      Distance of the physics area

      :type: float in [0, 20], default 0.0

   .. attribute:: fh_force

      Upward spring force, when inside the physics distance area

      :type: float in [0, 1], default 0.0

   .. attribute:: friction

      Coulomb friction coefficient, when inside the physics distance area

      :type: float in [0, 100], default 0.0

   .. attribute:: use_fh_normal

      Align dynamic game objects along the surface normal, when inside the physics distance area

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

   * :class:`Material.physics`

