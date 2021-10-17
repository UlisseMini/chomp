"""
Goal: Compile to neural network.
I can also train approximators for the program and see how they compare.
"""

import ast
import numpy as np
from typing import Dict

def relu(x):
    return np.maximum(0, x)


class Network():
    def __init__(self, weights, biases):
        assert(len(weights) == len(biases))
        dtype = np.int32
        self.weights = np.array(weights, dtype=dtype)
        self.biases = np.array(biases, dtype=dtype)

    def forward(self, x):
        x = np.array(x)
        for W, b in zip(self.weights, self.biases):
            x = W @ x + b

        return x


def simplify(op: ast.Expr):
    "Simplify a linear expr into m*x + b form"
    if isinstance(op, ast.Constant):
        return op
    if isinstance(op, ast.Name):
        return op
    elif isinstance(op, ast.Add):
        return op
    elif isinstance(op, ast.Mult):
        return op
    else:
        raise ValueError(f'unknown op {op}')

class Compiler():
    def __init__(self):
        self.weights = []
        self.biases = []

    def compile(self, source: str):
        tree = ast.parse(source)
        fn = tree.body[0]
        assert isinstance(fn, ast.FunctionDef)
        self.fndef(fn)


    def fndef(self, fn: ast.FunctionDef):
        # get arg names
        args = [arg.arg for arg in fn.args.args]

        self.weights = [[1] * len(args)]
        self.biases = [0] * len(args)
        self.vindex: Dict[str,int] = {arg: i for i, arg in enumerate(args)}

        ret = fn.body[0]
        assert isinstance(ret, ast.Return)

        op = ret.value
        assert isinstance(op, ast.BinOp)
        self.binop(op)


    def binop(self, op: ast.BinOp):
        if isinstance(op.op, ast.Add):
            assert isinstance(op.left, ast.Name)
            assert isinstance(op.right, ast.Constant)

            variable = op.left.id
            constant = op.right.value
            vindex = self.vindex[variable]
            self.biases[vindex] += constant
        elif isinstance(op.op, ast.Mult):
            assert isinstance(op.left, ast.Name)
            assert isinstance(op.right, ast.Constant)

            variable = op.left.id
            constant = op.right.value
            vindex = self.vindex[variable]
            self.weights[0][vindex] *= constant
        else:
            raise ValueError(f'Unknown op {op.op}')


def compile(source: str) -> Network:
    compiler = Compiler()
    compiler.compile(source)
    return Network(compiler.weights, compiler.biases)


