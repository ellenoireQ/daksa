from daksa.matrix import Matrix

mt = Matrix([[2, 3], [2, 4]])

"""
Addition test for matrices of the same order
"""
assert mt + mt == Matrix(
    [[4, 6], [4, 8]]
), f"Addition is wrong, actual value is: {mt+mt}"


"""
Subtraction test for matrices of the same order
"""
assert mt - mt == Matrix(
    [[0, 0], [0, 0]]
), f"Subtraction is wrong, actual value is: {mt-mt}"

"""
Multiplication test for matrices of the same order
"""
print(mt * mt)

"""
Multiplication test for matrices of the same order
"""
assert (2 * 3.14) * mt == Matrix(
    [[12.56, 18.84], [12.56, 25.12]]
), f"Subtraction is wrong, actual value is: {(2 * 3.14) * mt}"
