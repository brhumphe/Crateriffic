IDMaterials(bpy_struct)
=======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: IDMaterials(bpy_struct)

   Collection of materials

   .. method:: append(material)

      Add a new material to the data-block

      :arg material:

         Material to add

      :type material: :class:`Material`

   .. method:: pop(index=-1, update_data=False)

      Remove a material from the data-block

      :arg index:

         Index of material to remove

      :type index: int in [-32766, 32766], (optional)
      :arg update_data:

         Update data by re-adjusting the material slots assigned

      :type update_data: boolean, (optional)
      :return:

         Material to remove

      :rtype: :class:`Material`

   .. method:: clear(update_data=False)

      Remove all materials from the data-block

      :arg update_data:

         Update data by re-adjusting the material slots assigned

      :type update_data: boolean, (optional)

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

   * :class:`Curve.materials`
   * :class:`Mesh.materials`
   * :class:`MetaBall.materials`

