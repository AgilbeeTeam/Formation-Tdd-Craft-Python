import unittest

from test_package import echo_fib


class MyTestCase(unittest.TestCase):
    def test_fibo_n_equal_0(self):
        self.assertEqual(0, echo_fib.fibonacci(0))  # add assertion here


if __name__ == '__main__':
    unittest.main()
