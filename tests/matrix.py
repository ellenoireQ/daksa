from daksa.matrix import Matrix

mt = Matrix([[2, 3], [2, 4]])


def test_addition():
    """Addition matrices of the same order."""
    result = mt + mt
    expected = Matrix([[4, 6], [4, 8]])
    assert result == expected, f"Addition is wrong, actual value is: {result}"


def test_subtraction():
    """Subtraction matrices of the same order."""
    result = mt - mt
    expected = Matrix([[0, 0], [0, 0]])
    assert result == expected, f"Subtraction is wrong, actual value is: {result}"


def test_elementwise_multiplication():
    """Elementwise multiplication matrices of the same order."""
    result = mt * mt
    assert result == Matrix(
        [[4, 9], [4, 16]]
    ), f"Multiplication is wrong, actual value is: {result}"


def test_scalar_multiplication():
    """Multiplication of a matrix by a scalar."""
    scalar = 2 * 3.14
    result = scalar * mt
    expected = Matrix([[12.56, 18.84], [12.56, 25.12]])
    assert (
        result == expected
    ), f"Scalar multiplication is wrong, actual value is: {result}"


def test_matrix_multiplication():
    """Matrix multiplication using row and column dot products."""
    left = Matrix([[1, 2, 3], [4, 5, 6]])
    right = Matrix([[7, 8], [9, 10], [11, 12]])

    assert left @ right == Matrix([[58, 64], [139, 154]])


def test_matrix_multiplication_requires_compatible_dimensions():
    """Matrix multiplication rejects incompatible dimensions."""
    try:
        Matrix([[1, 2]]) @ Matrix([[3, 4]])
    except ValueError as error:
        assert str(error) == "Matrices must have compatible dimensions"
    else:
        raise AssertionError("Expected incompatible matrix dimensions to fail")


if __name__ == "__main__":
    test_addition()
    test_subtraction()
    test_elementwise_multiplication()
    test_scalar_multiplication()
    test_matrix_multiplication()
    test_matrix_multiplication_requires_compatible_dimensions()
    print("All tests passed.")
