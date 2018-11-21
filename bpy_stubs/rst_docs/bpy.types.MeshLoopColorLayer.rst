MeshLoopColorLayer(bpy_struct)
==============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshLoopColorLayer(bpy_struct)

   Layer of vertex colors in a Mesh data-block

   .. attribute:: active

      Sets the layer as active for display and editing

      :type: boolean, default False

   .. attribute:: active_render

      Sets the layer as active for rendering

      :type: boolean, default False

   .. data:: data

      :type: :class:`bpy_prop_collection` of :class:`MeshLoopColor`, (readonly)

   .. attribute:: name

      Name of Vertex color layer

      :type: string, default "", (never None)

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

   * :class:`LoopColors.active`
   * :class:`LoopColors.new`
   * :class:`LoopColors.remove`
   * :class:`Mesh.vertex_colors`

