"""
Goal: Compile to neural network.
I can also train approximators for the program and see how they compare.
"""

import ast
import numpy as np

def relu(x):
    return np.maximum(0, x)


class Network:
    def __init__(self, weights: np.ndarray, biases: np.ndarray):
        assert(len(weights) == len(biases))
        self.weights = weights
        self.biases = biases

    def forward(self, x: np.ndarray) -> np.ndarray:
        for W, b in zip(self.weights, self.biases):
            x = relu(W @ x + b)

        return x

def compile(tree: ast.AST) -> Network:
    pass


def main():
    import sys
    s = sys.stdin.read()
    tree = ast.parse(s)
    print(compile(tree))


if __name__ == '__main__':
    main()
