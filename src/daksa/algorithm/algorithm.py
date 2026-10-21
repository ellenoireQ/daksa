class Algorithm:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate
        self.weight = 0.0
        self.bias = 0.0
        self.input = 0.0

    def LinearRegression(self, weight: float, bias: float, input: float):
        self.weight = weight
        self.bias = bias
        self.input = input

        return (self.weight * self.input) + self.bias
