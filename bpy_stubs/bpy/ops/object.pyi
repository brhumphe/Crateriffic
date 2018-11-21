from typing import Optional

__all__ = ['mode_set']


def mode_set(*, mode: str, toggle: Optional[bool] = False) -> None:
    """
   Sets the object interaction mode

   :arg mode:

      Mode

      * ``OBJECT`` Object Mode.
      * ``EDIT`` Edit Mode.
      * ``POSE`` Pose Mode.
      * ``SCULPT`` Sculpt Mode.
      * ``VERTEX_PAINT`` Vertex Paint.
      * ``WEIGHT_PAINT`` Weight Paint.
      * ``TEXTURE_PAINT`` Texture Paint.
      * ``PARTICLE_EDIT`` Particle Edit.
      * ``GPENCIL_EDIT`` Edit Strokes, Edit Grease Pencil Strokes.

   :type mode: enum in ['OBJECT', 'EDIT', 'POSE', 'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT', 'PARTICLE_EDIT', 'GPENCIL_EDIT'], (optional)
   :arg toggle:

      Toggle

   :type toggle: boolean, (optional)
    """
    ...