CYCLES(RenderEngine)
====================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`RenderEngine`

.. class:: CYCLES(RenderEngine)

   

   .. method:: bake(scene, obj, pass_type, pass_filter, object_id, pixel_array, num_pixels, depth, result)

   .. method:: render(scene)

   .. method:: update(data, scene)

   .. method:: update_render_passes(scene, srl)

   .. method:: update_script_node(node)

   .. method:: view_draw(context)

   .. method:: view_update(context)

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`RenderEngine.is_animation`
   * :class:`RenderEngine.is_preview`
   * :class:`RenderEngine.camera_override`
   * :class:`RenderEngine.layer_override`
   * :class:`RenderEngine.tile_x`
   * :class:`RenderEngine.tile_y`
   * :class:`RenderEngine.resolution_x`
   * :class:`RenderEngine.resolution_y`
   * :class:`RenderEngine.render`
   * :class:`RenderEngine.use_highlight_tiles`
   * :class:`RenderEngine.bl_idname`
   * :class:`RenderEngine.bl_label`
   * :class:`RenderEngine.bl_use_preview`
   * :class:`RenderEngine.bl_use_texture_preview`
   * :class:`RenderEngine.bl_use_postprocess`
   * :class:`RenderEngine.bl_use_shading_nodes`
   * :class:`RenderEngine.bl_use_shading_nodes_custom`
   * :class:`RenderEngine.bl_use_exclude_layers`
   * :class:`RenderEngine.bl_use_save_buffers`
   * :class:`RenderEngine.bl_use_spherical_stereo`

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
   * :class:`RenderEngine.update`
   * :class:`RenderEngine.render`
   * :class:`RenderEngine.bake`
   * :class:`RenderEngine.view_update`
   * :class:`RenderEngine.view_draw`
   * :class:`RenderEngine.update_script_node`
   * :class:`RenderEngine.tag_redraw`
   * :class:`RenderEngine.tag_update`
   * :class:`RenderEngine.update_render_passes`
   * :class:`RenderEngine.begin_result`
   * :class:`RenderEngine.update_result`
   * :class:`RenderEngine.end_result`
   * :class:`RenderEngine.add_pass`
   * :class:`RenderEngine.test_break`
   * :class:`RenderEngine.active_view_get`
   * :class:`RenderEngine.active_view_set`
   * :class:`RenderEngine.camera_shift_x`
   * :class:`RenderEngine.camera_model_matrix`
   * :class:`RenderEngine.use_spherical_stereo`
   * :class:`RenderEngine.update_stats`
   * :class:`RenderEngine.frame_set`
   * :class:`RenderEngine.update_progress`
   * :class:`RenderEngine.update_memory_stats`
   * :class:`RenderEngine.report`
   * :class:`RenderEngine.error_set`
   * :class:`RenderEngine.bind_display_space_shader`
   * :class:`RenderEngine.unbind_display_space_shader`
   * :class:`RenderEngine.support_display_space_shader`
   * :class:`RenderEngine.register_pass`

