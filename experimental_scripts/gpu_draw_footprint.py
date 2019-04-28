import bpy
import gpu
from gpu_extras.batch import batch_for_shader
import numpy as np


#coords = [(1, 1, 1), (-2, 0, 0), (-2, -1, 3), (0, 1, 1)]
coords = np.genfromtxt('/Users/admin/Projects/Crateriffic/test.csv', delimiter=',')
print(coords)
shader = gpu.shader.from_builtin('3D_UNIFORM_COLOR')
batch = batch_for_shader(shader, 'LINES', {"pos": coords})


def draw():
    shader.bind()
    shader.uniform_float("color", (1, 0, 1, 1))
    batch.draw(shader)


bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')