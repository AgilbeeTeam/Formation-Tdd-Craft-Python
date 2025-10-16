import unittest

from exercice import my_math_lib


class MyTestCase(unittest.TestCase):
    def test_fibo_n_equal_0(self):
        self.assertEqual(0, my_math_lib.fibonacci(0))  # add assertion here


if __name__ == '__main__':
    unittest.main()
