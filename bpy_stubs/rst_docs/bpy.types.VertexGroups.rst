VertexGroups(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: VertexGroups(bpy_struct)

   Collection of vertex groups

   .. data:: active

      Vertex groups of the object

      :type: :class:`VertexGroup`, (readonly)

   .. attribute:: active_index

      Active index in vertex group array

      :type: int in [0, 32767], default 0

   .. method:: new(name="Group")

      Add vertex group to object

      :arg name:

         Vertex group name

      :type name: string, (optional, never None)
      :return:

         New vertex group

      :rtype: :class:`VertexGroup`

   .. method:: remove(group)

      Delete vertex group from object

      :arg group:

         Vertex group to remove

      :type group: :class:`VertexGroup`, (never None)

   .. method:: clear()

      Delete all vertex groups from object


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

   * :class:`Object.vertex_groups`

