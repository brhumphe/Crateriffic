NodeTreeOutputs(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: NodeTreeOutputs(bpy_struct)

   Collection of Node Tree Sockets

   .. method:: new(type, name)

      Add a socket to this node tree

      :arg type:

         Type, Data type

      :type type: string, (never None)
      :arg name:

         Name

      :type name: string, (never None)
      :return:

         New socket

      :rtype: :class:`NodeSocketInterface`

   .. method:: remove(socket)

      Remove a socket from this node tree

      :arg socket:

         The socket to remove

      :type socket: :class:`NodeSocketInterface`

   .. method:: clear()

      Remove all sockets from this node tree


   .. method:: move(from_index, to_index)

      Move a socket to another position

      :arg from_index:

         From Index, Index of the socket to move

      :type from_index: int in [0, inf]
      :arg to_index:

         To Index, Target index for the socket

      :type to_index: int in [0, inf]

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

   * :class:`NodeTree.outputs`

