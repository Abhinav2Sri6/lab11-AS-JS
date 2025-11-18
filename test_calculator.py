# https://github.com/Abhinav2Sri6/lab11-AS-JS
# Partner 1: Abhinav Sriram
# Partner 2: Jayson Sandy

import unittest
import math
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-5, 2), -3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(5, 10), -5)
        self.assertEqual(sub(0, 0), 0)

    ##########################

    ######## Partner 1
    def test_multiply(self):
        pass  # Partner 1 will fill this

    def test_divide(self):
        pass  # Partner 1 will fill this

    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 100)

    def test_logarithm(self):
        self.assertAlmostEqual(log(10, 100), 2.0)
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(math.e, math.e), 1.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(0, 5)
        with self.assertRaises(ValueError):
            log(-2, 10)
        with self.assertRaises(ValueError):
            log(1, 10)
        with self.assertRaises(ValueError):
            log(10, -5)
        with self.assertRaises(ValueError):
            log(10, 0)

    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):
        pass  # Partner 1 will fill this

    def test_hypotenuse(self):
        pass  # Partner 1 will fill this

    def test_sqrt(self):
        pass  # Partner 1 will fill this
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()