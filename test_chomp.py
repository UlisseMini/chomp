import unittest
import chomp

class Basic(unittest.TestCase):
    def test_basic(self):
        net = chomp.compile('def f(x): return x + 1')
        self.assertEqual(net.forward([5]), 6)


if __name__ == '__main__':
    unittest.main()
