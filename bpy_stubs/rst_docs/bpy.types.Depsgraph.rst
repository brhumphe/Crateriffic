Depsgraph(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Depsgraph(bpy_struct)

   

   .. method:: debug_graphviz(filename)

      debug_graphviz

      :arg filename:

         File Name, File in which to store graphviz debug output

      :type filename: string, (never None)

   .. method:: debug_rebuild()

      debug_rebuild


   .. method:: debug_stats()

      Report the number of elements in the Dependency Graph


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

   * :class:`Scene.depsgraph`

