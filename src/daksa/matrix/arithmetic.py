from __future__ import annotations

from collections.abc import Callable

Scalar = int | float
MatrixData = list[list[Scalar]]


def add_matrices(left: MatrixData, right: MatrixData) -> MatrixData:
    return _combine_matrices(left, right, lambda first, second: first + second)


def subtract_matrices(left: MatrixData, right: MatrixData) -> MatrixData:
    return _combine_matrices(left, right, lambda first, second: first - second)


def multiple_matrices(left: MatrixData, right: MatrixData) -> MatrixData:
    """Elementwise multiplication, or scalar multiplication if `left` is a number."""
    if isinstance(left, (int, float)):
        return [[left * value for value in row] for row in right]
    return _combine_matrices(left, right, lambda first, second: first * second)


def _combine_matrices(
    left: MatrixData,
    right: MatrixData,
    operation: Callable[[Scalar, Scalar], Scalar],
) -> MatrixData:
    if len(left) != len(right) or any(
        len(left_row) != len(right_row) for left_row, right_row in zip(left, right)
    ):
        raise ValueError("Matrices must have the same order")

    return [
        [operation(a, b) for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]
