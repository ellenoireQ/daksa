from __future__ import annotations

from numbers import Number

from .arithmetic import add_matrices, subtract_matrices, multiple_matrices
from .inverse import invert_matrix

MatrixData = list[list[Number]]


class Matrix:
    def __init__(self, listd: MatrixData | None = None):
        self.arrays: MatrixData = listd if listd is not None else []

    def array(self, listd: MatrixData) -> MatrixData:
        self.arrays = listd
        return self.arrays

    def __add__(self, other: Matrix) -> Matrix:
        return Matrix(add_matrices(self.arrays, other.arrays))

    def __sub__(self, other: Matrix) -> Matrix:
        return Matrix(subtract_matrices(self.arrays, other.arrays))

    def __mul__(self, other: Matrix) -> Matrix:
        return Matrix(multiple_matrices(self.arrays, other.arrays))

    def __rmul__(self, other: Number) -> Matrix:
        return Matrix(multiple_matrices(other, self.arrays))

    def inverse(self) -> Matrix:
        return Matrix(invert_matrix(self.arrays))

    def __repr__(self) -> str:
        return str(self.arrays)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        return self.arrays == other.arrays
