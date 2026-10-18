from __future__ import annotations

from numbers import Number

MatrixData = list[list[Number]]


def invert_matrix(matrix: MatrixData) -> MatrixData:
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0

    if height != 2 or width != 2:
        raise ValueError(
            f"Matrix with {width}x{height} doesn't support for 2x2 inverses!"
        )

    a, b = matrix[0]
    c, d = matrix[1]
    determinant = (a * d) - (b * c)

    if determinant == 0:
        raise ValueError(f"Matrix with {determinant} determinant cannot invertible!")

    return [[d / determinant, -b / determinant], [-c / determinant, a / determinant]]
