MeshSkinVertex(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshSkinVertex(bpy_struct)

   Per-vertex skin data for use with the Skin modifier

   .. attribute:: radius

      Radius of the skin

      :type: float array of 2 items in [0, inf], default (0.0, 0.0)

   .. attribute:: use_loose

      If vertex has multiple adjacent edges, it is hulled to them directly

      :type: boolean, default False

   .. attribute:: use_root

      Vertex is a root for rotation calculations and armature generation

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

   * :class:`MeshSkinVertexLayer.data`

