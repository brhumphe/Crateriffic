RenderResult(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RenderResult(bpy_struct)

   Result of rendering, including all layers and passes

   .. data:: layers

      :type: :class:`bpy_prop_collection` of :class:`RenderLayer`, (readonly)

   .. data:: resolution_x

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: resolution_y

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: views

      :type: :class:`bpy_prop_collection` of :class:`RenderView`, (readonly)

   .. method:: load_from_file(filename)

      Copies the pixels of this render result from an image file

      :arg filename:

         File Name, Filename to load into this render tile, must be no smaller than the render result

      :type filename: string, (never None)

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

   * :class:`RenderEngine.begin_result`
   * :class:`RenderEngine.end_result`
   * :class:`RenderEngine.update_result`

