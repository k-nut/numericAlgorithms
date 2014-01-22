#!/usr/bin/python3

import unittest

from spline import Spline


class TestBasicSpline(unittest.TestCase):
    def test_baisc(self):
        x = [-3, -2, -1, 0, 1, 2, 3]
        y = [5, 3, 1, 0, -1, 2, -2]
        firstderivate = -1
        lastderivate = 1
        spline = Spline(x, y, firstderivate, lastderivate)
        self.assertEqual(spline.lambdas, [1, 0.5, 0.5, 0.5, 0.5, 0.5])
        self.assertEqual(spline.mys, [0, 0.5, 0.5, 0.5, 0.5, 1])


if __name__ == "__main__":
    unittest.main()
