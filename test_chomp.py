import unittest
import ast
import chomp

class Compiler(unittest.TestCase):
    def test_add(self):
        net = chomp.compile('def f(x): return x + 1')
        self.assertEqual(net.forward([5]), 6)
        self.assertEqual(net.forward([7]), 8)
        self.assertEqual(net.forward([-5]), -4)


    def test_mul(self):
        net = chomp.compile('def f(x): return x * 2')
        self.assertEqual(net.forward([5]), 10)
        self.assertEqual(net.forward([2]), 4)
        self.assertEqual(net.forward([-2]), -4)


    # def test_add_mul_nested(self):
    #     net = chomp.compile('def f(x): return 2*x + 3')
    #     self.assertEqual(net.forward([2]), 7)
    #     self.assertEqual(net.forward([-2]), -1)
    #     self.assertEqual(net.forward([-3]), -3)


    def test_simplify(self):
        tests = [
            ('x*3 + 2', '3*x + 2'),
            ('x', '1*x + 0'),
            ('x + x', '2*x + 0'),
            ('x * (1 + 2) + 4', '3*x + 4')
        ]
        for expr, want in tests:
            tree = ast.parse(expr)
            expr = tree.body[0]
            assert isinstance(expr, ast.Expr)
            got = ast.unparse(chomp.simplify(expr))
            self.assertEqual(got, want)

    # def test_collatz(self):
    #     net = chomp.compile('''
    #     def f(x):
    #         if x % 2 == 0:
    #             return 0.5*x
    #         else:
    #             return 3*x + 1
    #     ''')
    #     self.assertEqual(net.forward([2]), 1)
    #     self.assertEqual(net.forward([1]), 4)
    #     self.assertEqual(net.forward([5]), 16)

if __name__ == '__main__':
    unittest.main()
