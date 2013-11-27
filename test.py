#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import random
from sol import Polynom, createPolynomFromNull


class TestPolynomFunction(unittest.TestCase):

    def setUp(self):
        self.polynom1 = Polynom([0, 1])  # x
        self.polynom2 = Polynom([2])     # 2
        self.polynom3 = Polynom([-2, 0, 1])  # x² - 2
        self.polynom4 = Polynom([-6, 11, -6, 1])

    def test_representation(self):
        self.assertEqual(self.polynom1.__repr__(), "0x^0 + 1x^1")
        self.assertEqual(self.polynom2.__repr__(), "2x^0")
        self.assertEqual(self.polynom3.__repr__(), "-2x^0 + 0x^1 + 1x^2")
        self.assertEqual(self.polynom4.__repr__(), "-6x^0 + 11x^1 + -6x^2 + 1x^3")

    def test_calculating_value(self):
        self.assertEqual(self.polynom1.calculate_at(1), 1)
        self.assertEqual(self.polynom1.calculate_at(-77), -77)

        self.assertEqual(self.polynom2.calculate_at(1), 2)
        self.assertEqual(self.polynom2.calculate_at(random.randint(-1000, 1000)), 2)

        self.assertEqual(self.polynom3.calculate_at(1), -1)

        self.assertEqual(self.polynom4.calculate_at(1), 0)
        self.assertEqual(self.polynom4.calculate_at(2), 0)
        self.assertEqual(self.polynom4.calculate_at(3), 0)


class TestCreationOfPolynomFromNullFunction(unittest.TestCase):

    def setUp(self):
        self.polynom1 = createPolynomFromNull([1, 2, 3])
        self.polynom2 = createPolynomFromNull([1])

    def test_representation(self):
        self.assertEqual(self.polynom1.__repr__(), "-6x^0 + 11x^1 + -6x^2 + 1x^3")
        self.assertEqual(self.polynom2.__repr__(), "-1x^0 + 1x^1")

    def test_calculating_value(self):
        self.assertEqual(self.polynom1.calculate_at(1), 0)
        self.assertEqual(self.polynom1.calculate_at(2), 0)
        self.assertEqual(self.polynom1.calculate_at(3), 0)


class TestAddingTwoPolynoms(unittest.TestCase):

    def setUp(self):
        self.polynom1 = Polynom([0, 1])  # x
        self.polynom2 = Polynom([2])     # 2
        self.polynom3 = Polynom([-2, 0, 1])  # x² - 2
        self.polynom4 = Polynom([-6, 11, -6, 1])

    def test_adding(self):
        summedPolynom = self.polynom1 + self.polynom2
        referncePolynom = Polynom([2, 1])
        self.assertEqual(summedPolynom.__repr__(), referncePolynom.__repr__())


if __name__ == "__main__":
    unittest.main()
