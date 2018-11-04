import bpy


def getView3dAreaAndRegion(context):
    for area in context.screen.areas:
        if area.type == "VIEW_3D":
            for space in area.spaces:
                if space.type == "VIEW_3D":
                    space.use_occlude_geometry = True
            for region in area.regions:
                if region.type == "WINDOW":
                    return area, region


def select_border(context, view3dAreaAndRegion=None, extend=True):
    if not view3dAreaAndRegion:
        view3dAreaAndRegion = getView3dAreaAndRegion(context)
    view3dArea, view3dRegion = view3dAreaAndRegion
    context_copy = context.copy()
    context_copy['area'] = view3dArea
    context_copy['region'] = view3dRegion
    # bpy.ops.mesh.hide(unselected=False)
    # bpy.context.space_data.use_occlude_geometry = True

    bpy.ops.view3d.select_border(context_copy,
                                 gesture_mode=3,
                                 xmin=0,
                                 xmax=view3dArea.width,
                                 ymin=0,
                                 ymax=view3dArea.height,
                                 extend=extend)
    return view3dAreaAndRegion


select_border(bpy.context)
