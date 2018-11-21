ParticleKey(bpy_struct)
=======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ParticleKey(bpy_struct)

   Key location for a particle over time

   .. attribute:: angular_velocity

      Key angular velocity

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: location

      Key location

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: rotation

      Key rotation quaternion

      :type: float array of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: time

      Time of key over the simulation

      :type: float in [0, inf], default 0.0

   .. attribute:: velocity

      Key velocity

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

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

   * :class:`Particle.particle_keys`

