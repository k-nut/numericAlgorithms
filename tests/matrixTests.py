#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ..matrix import Matrix


class TestBaiscMatrix(unittest.TestCase):
    columns = 2
    rows = 3
    matrix = Matrix(columns, rows)

    def test_representation(self):
        self.assertEqual(self.matrix.columnCount, 2)
        self.assertEqual(self.matrix.rowCount, 3)

        for column in range(self.columns):
            for row in range(self.rows):
                self.assertEqual(self.matrix.getValue(column, row), 0)

"""
    def test_filling_matrix(self):
        self.matrix.setColumn(1, [1, 2, 3])
"""

if __name__ == "__main__":
    unittest.main()
