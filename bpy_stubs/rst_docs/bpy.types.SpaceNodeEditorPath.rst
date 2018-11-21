SpaceNodeEditorPath(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SpaceNodeEditorPath(bpy_struct)

   Get the node tree path as a string

   .. data:: to_string

      :type: string, default "", (readonly, never None)

   .. method:: clear()

      Reset the node tree path


   .. method:: start(node_tree)

      Set the root node tree

      :arg node_tree:

         Node Tree

      :type node_tree: :class:`NodeTree`

   .. method:: append(node_tree, node=None)

      Append a node group tree to the path

      :arg node_tree:

         Node Tree, Node tree to append to the node editor path

      :type node_tree: :class:`NodeTree`
      :arg node:

         Node, Group node linking to this node tree

      :type node: :class:`Node`, (optional)

   .. method:: pop()

      Remove the last node tree from the path


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

   * :class:`SpaceNodeEditor.path`

