#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ..matrix import Matrix

"""
class TestBaiscMatrix(unittest.TestCase):
    def test_representation(self):
        columns = 2
        rows = 3
        matrix = Matrix(columns, rows)
        self.assertEqual(matrix.columnCount, 2)
        self.assertEqual(matrix.rowCount, 3)

        for column in range(columns):
            for row in range(rows):
                self.assertEqual(matrix.getValue(column, row), 0)
"""

class TestSettingValues(unittest.TestCase):
    def test_filling_matrix(self):
        columns = 2
        rows = 3
        matrix = Matrix(columns, rows)
        #self.assertRaises(ValueError, matrix.setColumn, 1, [1, 2, 3, 4])
        self.assertRaises(ValueError, matrix.setRow, 1, [1, 2, 3])
        """
        matrix.setColumn(1, [1, 2, 3])
        matrix.setColumn(2, [4, 5, 6])
        """
        matrix.setRow(2, [2, 5])
        print(matrix)

if __name__ == "__main__":
    unittest.main()
