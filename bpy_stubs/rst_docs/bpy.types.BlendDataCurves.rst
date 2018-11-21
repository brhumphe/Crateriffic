BlendDataCurves(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataCurves(bpy_struct)

   Collection of curves

   .. data:: is_updated

      :type: boolean, default False, (readonly)

   .. method:: new(name, type)

      Add a new curve to the main database

      :arg name:

         New name for the data-block

      :type name: string, (never None)
      :arg type:

         Type, The type of curve to add

      :type type: enum in ['CURVE', 'SURFACE', 'FONT']
      :return:

         New curve data-block

      :rtype: :class:`Curve`

   .. method:: remove(curve, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a curve from the current blendfile

      :arg curve:

         Curve to remove

      :type curve: :class:`Curve`, (never None)
      :arg do_unlink:

         Unlink all usages of this curve before deleting it (WARNING: will also delete objects instancing that curve data)

      :type do_unlink: boolean, (optional)
      :arg do_id_user:

         Decrement user counter of all datablocks used by this curve data

      :type do_id_user: boolean, (optional)
      :arg do_ui_user:

         Make sure interface does not reference this curve data

      :type do_ui_user: boolean, (optional)

   .. method:: tag(value)

      tag

      :arg value:

         Value

      :type value: boolean

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

   * :class:`BlendData.curves`

