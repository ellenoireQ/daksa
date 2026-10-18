from __future__ import annotations

from collections.abc import Callable
from numbers import Number

MatrixData = list[list[Number]]


def add_matrices(left: MatrixData, right: MatrixData) -> MatrixData:
    return _combine_matrices(left, right, lambda first, second: first + second)


def subtract_matrices(left: MatrixData, right: MatrixData) -> MatrixData:
    return _combine_matrices(left, right, lambda first, second: first - second)


def multiple_matrices(left: MatrixData, right: MatrixData) -> MatrixData:
    return _combine_matrices(left, right, lambda first, second: first * second)


def _combine_matrices(
    left: MatrixData,
    right: MatrixData,
    operation: Callable[[Number, Number], Number],
) -> MatrixData:
    return [
        [
            operation(left[row][column], right[row][column])
            for column in range(len(left[row]))
        ]
        for row in range(len(left))
    ]
