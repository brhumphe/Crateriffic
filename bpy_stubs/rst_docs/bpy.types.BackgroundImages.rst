BackgroundImages(bpy_struct)
============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BackgroundImages(bpy_struct)

   Collection of background images

   .. method:: new()

      Add new background image

      :return:

         Image displayed as viewport background

      :rtype: :class:`BackgroundImage`

   .. method:: remove(image)

      Remove background image

      :arg image:

         Image displayed as viewport background

      :type image: :class:`BackgroundImage`, (never None)

   .. method:: clear()

      Remove all background images


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

   * :class:`SpaceView3D.background_images`

