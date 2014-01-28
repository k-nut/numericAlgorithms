#!/usr/bin/python3

import unittest

from spline import Spline


class TestBasicSpline(unittest.TestCase):
    def test_baisc(self):
        x = [0, 1, 2, 3]
        y = [7, 3, 5, -2]
        firstderivate = -1
        lastderivate = 0
        spline = Spline(x, y, firstderivate, lastderivate)
        self.assertEqual(spline.lambdas, [1, 0.5, 0.5])
        self.assertEqual(spline.mys, [False, 0.5, 0.5, 1])
        self.assertEqual(spline.ds, [-18.0, 18.0, -27.0, 42.0])
        self.assertEqual(spline.new_lambdas, [0.5, 2.0 / 7, 7.0 / 26])
        #self.assertEqual(spline.new_ds, [-9, 90 / 7.0, -18.0, 1])  # die 1 ist
        #falsch und muss ersetzt werden
        # expectedMis = [104 / 3.0, -82 / 3.0, 62 /3.0, -58 / 3.0]
        expectedMis = [-58 / 3.0, 62 / 3, -82 / 3.0, 104 / 3.0]
        for i in range(len(expectedMis)):
            self.assertAlmostEqual(expectedMis[i], spline.Mis[i])

if __name__ == "__main__":
    unittest.main()
