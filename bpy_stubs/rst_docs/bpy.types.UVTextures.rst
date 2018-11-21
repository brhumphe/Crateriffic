UVTextures(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UVTextures(bpy_struct)

   Collection of UV maps

   .. attribute:: active

      Active UV Map

      :type: :class:`MeshTexturePolyLayer`

   .. attribute:: active_index

      Active UV Map index

      :type: int in [0, inf], default 0

   .. method:: new(name="UVMap")

      Add a UV map layer to Mesh

      :arg name:

         UV map name

      :type name: string, (optional, never None)
      :return:

         The newly created layer

      :rtype: :class:`MeshTexturePolyLayer`

   .. method:: remove(layer)

      Remove a vertex color layer

      :arg layer:

         The layer to remove

      :type layer: :class:`MeshTexturePolyLayer`, (never None)

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

   * :class:`Mesh.uv_textures`

