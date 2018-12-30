bl_info = {
    "name": "Crateriffic",
    "author": "Benjamin Humpherys",
    "location": "View3D > Tools > Crateriffic",
    "category": "Development"
}

# When bpy is already in local, we know this is not the initial import...
if "bpy" in locals():
    print("===========Reloading Crateriffic============")
    # ...so we need to reload our submodule(s) using importlib
    import importlib
    if "HighlightFacing" in locals():
        importlib.reload(HighlightFacing)
        
    if "rayscan" in locals():
        importlib.reload(rayscan)


# This is only relevant on first run, on later reloads those modules
# are already in locals() and those statements do not do anything.
import bpy
from . import HighlightFacing, rayscan
classes = [HighlightFacing.HighlightFacingOperator,
            rayscan.RayScanOperator]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    
def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
