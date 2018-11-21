from typing import Sequence, Union

__all__ = ['Vector']


class Vector:
    def __init__(self, seq: VectorLike):
        ...

# TODO: Update to include Euler, Quaternion, Matrix
    def rotate(self, other: VectorLike):
        """
        Rotate the vector by a rotation value.
        :arg other: rotation component of mathutils value
        :type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`
        """
        ...


VectorLike = Union[Sequence[Union[int, float]], Vector]
