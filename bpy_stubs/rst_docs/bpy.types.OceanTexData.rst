OceanTexData(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: OceanTexData(bpy_struct)

   Ocean Texture settings

   .. attribute:: ocean_object

      Object containing the ocean modifier

      :type: :class:`Object`

   .. attribute:: output

      The data that is output by the texture

      * ``DISPLACEMENT`` Displacement, Output XYZ displacement in RGB channels.
      * ``FOAM`` Foam, Output Foam (wave overlap) amount in single channel.
      * ``JPLUS`` Eigenvalues, Positive Eigenvalues.
      * ``EMINUS`` Eigenvectors (-), Negative Eigenvectors.
      * ``EPLUS`` Eigenvectors (+), Positive Eigenvectors.

      :type: enum in ['DISPLACEMENT', 'FOAM', 'JPLUS', 'EMINUS', 'EPLUS'], default 'DISPLACEMENT'

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

   * :class:`OceanTexture.ocean`

