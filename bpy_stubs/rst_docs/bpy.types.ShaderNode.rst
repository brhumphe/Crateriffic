ShaderNode(NodeInternal)
========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`

subclasses --- 
:class:`ShaderNodeAddShader`, :class:`ShaderNodeAmbientOcclusion`, :class:`ShaderNodeAttribute`, :class:`ShaderNodeBackground`, :class:`ShaderNodeBlackbody`, :class:`ShaderNodeBrightContrast`, :class:`ShaderNodeBsdfAnisotropic`, :class:`ShaderNodeBsdfDiffuse`, :class:`ShaderNodeBsdfGlass`, :class:`ShaderNodeBsdfGlossy`, :class:`ShaderNodeBsdfHair`, :class:`ShaderNodeBsdfPrincipled`, :class:`ShaderNodeBsdfRefraction`, :class:`ShaderNodeBsdfToon`, :class:`ShaderNodeBsdfTranslucent`, :class:`ShaderNodeBsdfTransparent`, :class:`ShaderNodeBsdfVelvet`, :class:`ShaderNodeBump`, :class:`ShaderNodeCameraData`, :class:`ShaderNodeCombineHSV`, :class:`ShaderNodeCombineRGB`, :class:`ShaderNodeCombineXYZ`, :class:`ShaderNodeEmission`, :class:`ShaderNodeExtendedMaterial`, :class:`ShaderNodeFresnel`, :class:`ShaderNodeGamma`, :class:`ShaderNodeGeometry`, :class:`ShaderNodeGroup`, :class:`ShaderNodeHairInfo`, :class:`ShaderNodeHoldout`, :class:`ShaderNodeHueSaturation`, :class:`ShaderNodeInvert`, :class:`ShaderNodeLampData`, :class:`ShaderNodeLayerWeight`, :class:`ShaderNodeLightFalloff`, :class:`ShaderNodeLightPath`, :class:`ShaderNodeMapping`, :class:`ShaderNodeMaterial`, :class:`ShaderNodeMath`, :class:`ShaderNodeMixRGB`, :class:`ShaderNodeMixShader`, :class:`ShaderNodeNewGeometry`, :class:`ShaderNodeNormal`, :class:`ShaderNodeNormalMap`, :class:`ShaderNodeObjectInfo`, :class:`ShaderNodeOutput`, :class:`ShaderNodeOutputLamp`, :class:`ShaderNodeOutputLineStyle`, :class:`ShaderNodeOutputMaterial`, :class:`ShaderNodeOutputWorld`, :class:`ShaderNodeParticleInfo`, :class:`ShaderNodeRGB`, :class:`ShaderNodeRGBCurve`, :class:`ShaderNodeRGBToBW`, :class:`ShaderNodeScript`, :class:`ShaderNodeSeparateHSV`, :class:`ShaderNodeSeparateRGB`, :class:`ShaderNodeSeparateXYZ`, :class:`ShaderNodeSqueeze`, :class:`ShaderNodeSubsurfaceScattering`, :class:`ShaderNodeTangent`, :class:`ShaderNodeTexBrick`, :class:`ShaderNodeTexChecker`, :class:`ShaderNodeTexCoord`, :class:`ShaderNodeTexEnvironment`, :class:`ShaderNodeTexGradient`, :class:`ShaderNodeTexImage`, :class:`ShaderNodeTexMagic`, :class:`ShaderNodeTexMusgrave`, :class:`ShaderNodeTexNoise`, :class:`ShaderNodeTexPointDensity`, :class:`ShaderNodeTexSky`, :class:`ShaderNodeTexVoronoi`, :class:`ShaderNodeTexWave`, :class:`ShaderNodeTexture`, :class:`ShaderNodeUVAlongStroke`, :class:`ShaderNodeUVMap`, :class:`ShaderNodeValToRGB`, :class:`ShaderNodeValue`, :class:`ShaderNodeVectorCurve`, :class:`ShaderNodeVectorMath`, :class:`ShaderNodeVectorTransform`, :class:`ShaderNodeVolumeAbsorption`, :class:`ShaderNodeVolumeScatter`, :class:`ShaderNodeWavelength`, :class:`ShaderNodeWireframe`

.. class:: ShaderNode(NodeInternal)

   Material shader node

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Node.type`
   * :class:`Node.location`
   * :class:`Node.width`
   * :class:`Node.width_hidden`
   * :class:`Node.height`
   * :class:`Node.dimensions`
   * :class:`Node.name`
   * :class:`Node.label`
   * :class:`Node.inputs`
   * :class:`Node.outputs`
   * :class:`Node.internal_links`
   * :class:`Node.parent`
   * :class:`Node.use_custom_color`
   * :class:`Node.color`
   * :class:`Node.select`
   * :class:`Node.show_options`
   * :class:`Node.show_preview`
   * :class:`Node.hide`
   * :class:`Node.mute`
   * :class:`Node.show_texture`
   * :class:`Node.shading_compatibility`
   * :class:`Node.bl_idname`
   * :class:`Node.bl_label`
   * :class:`Node.bl_description`
   * :class:`Node.bl_icon`
   * :class:`Node.bl_static_type`
   * :class:`Node.bl_width_default`
   * :class:`Node.bl_width_min`
   * :class:`Node.bl_width_max`
   * :class:`Node.bl_height_default`
   * :class:`Node.bl_height_min`
   * :class:`Node.bl_height_max`

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
   * :class:`Node.socket_value_update`
   * :class:`Node.is_registered_node_type`
   * :class:`Node.poll`
   * :class:`Node.poll_instance`
   * :class:`Node.update`
   * :class:`Node.insert_link`
   * :class:`Node.init`
   * :class:`Node.copy`
   * :class:`Node.free`
   * :class:`Node.draw_buttons`
   * :class:`Node.draw_buttons_ext`
   * :class:`Node.draw_label`
   * :class:`Node.poll`
   * :class:`NodeInternal.poll`
   * :class:`NodeInternal.poll_instance`
   * :class:`NodeInternal.update`
   * :class:`NodeInternal.draw_buttons`
   * :class:`NodeInternal.draw_buttons_ext`

