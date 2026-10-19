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


if __name__ == "__main__":
    test_addition()
    test_subtraction()
    test_elementwise_multiplication()
    test_scalar_multiplication()
    print("All tests passed.")
