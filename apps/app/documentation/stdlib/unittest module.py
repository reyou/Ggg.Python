# https://docs.python.org/3/tutorial/stdlib.html
"""The unittest module is not as effortless as the doctest module,
but it allows a more comprehensive set of tests to be
maintained in a separate file:"""
import unittest
import statistics


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(statistics.average([20, 30, 70]), 40.0)
        self.assertEqual(round(statistics.average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            statistics.average([])
        with self.assertRaises(TypeError):
            statistics.average(20, 30, 70)


unittest.main()  # Calling from the command line invokes all tests
