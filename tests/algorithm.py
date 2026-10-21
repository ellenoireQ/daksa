from daksa.algorithm.algorithm import Algorithm

alg = Algorithm()


def test_algorithm_linear_regression():
    """Calculate a prediction from a weight, feature, and bias."""
    assert alg.LinearRegression(weight=2, input=3, bias=1) == 7


if __name__ == "__main__":
    test_algorithm_linear_regression()
    print("All test passed.")
