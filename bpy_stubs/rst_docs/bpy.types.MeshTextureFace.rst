MeshTextureFace(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshTextureFace(bpy_struct)

   UV map and image texture for a face

   .. attribute:: image

      :type: :class:`Image`

   .. attribute:: uv

      :type: float array of 8 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

   .. attribute:: uv1

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: uv2

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: uv3

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: uv4

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: uv_raw

      Fixed size UV coordinates array

      :type: float array of 8 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

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

   * :class:`MeshTextureFaceLayer.data`

