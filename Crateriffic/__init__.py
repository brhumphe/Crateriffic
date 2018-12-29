bl_info = {
    "name": "Crateriffic",
    "author": "Benjamin Humpherys",
    "location": "View3D > Tools > Crateriffic",
    "category": "Development"
}

from .HighlightFacing import HighlightFacingOperator

import bpy

classes = [HighlightFacingOperator]

def register():
    for c in classes:
        bpy.register_class(c)
    
def unregister():
    for c in reversed(classes):
        bpy.unregister_class(c)

if __name__ == "__main__":
    register()
