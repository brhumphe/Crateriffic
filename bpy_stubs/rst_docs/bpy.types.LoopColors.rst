LoopColors(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: LoopColors(bpy_struct)

   Collection of vertex colors

   .. attribute:: active

      Active vertex color layer

      :type: :class:`MeshLoopColorLayer`

   .. attribute:: active_index

      Active vertex color index

      :type: int in [0, inf], default 0

   .. method:: new(name="Col")

      Add a vertex color layer to Mesh

      :arg name:

         Vertex color name

      :type name: string, (optional, never None)
      :return:

         The newly created layer

      :rtype: :class:`MeshLoopColorLayer`

   .. method:: remove(layer)

      Remove a vertex color layer

      :arg layer:

         The layer to remove

      :type layer: :class:`MeshLoopColorLayer`, (never None)

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

   * :class:`Mesh.vertex_colors`

