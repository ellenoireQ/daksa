from __future__ import annotations

from collections.abc import Callable

Scalar = int | float
MatrixData = list[list[Scalar]]


def add_matrices(left: MatrixData, right: MatrixData) -> MatrixData:
    return _combine_matrices(left, right, lambda first, second: first + second)


def subtract_matrices(left: MatrixData, right: MatrixData) -> MatrixData:
    return _combine_matrices(left, right, lambda first, second: first - second)


def multiple_matrices(left: MatrixData, right: MatrixData) -> MatrixData:
    return _combine_matrices(left, right, lambda first, second: first * second)


def _combine_matrices(
    left: MatrixData,
    right: MatrixData,
    operation: Callable[[Scalar, Scalar], Scalar],
) -> MatrixData:
    if isinstance(left, Scalar):
        opr = [
            [left * right[row][column] for column in range(len(right[row]))]
            for row in range(len(right))
        ]
    else:
        opr = [
            [
                operation(left[row][column], right[row][column])
                for column in range(len(left[row]))
            ]
            for row in range(len(left))
        ]

    return opr
