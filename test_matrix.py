#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from matrix import Matrix


class TestBaiscMatrix(unittest.TestCase):
    def test_representation(self):
        columns = 2
        rows = 3
        matrix = Matrix(rows, columns)
        self.assertEqual(matrix.columnCount, 2)
        self.assertEqual(matrix.rowCount, 3)

        for column in range(columns):
            for row in range(rows):
                self.assertEqual(matrix.getValue(column, row), 0)


class TestSettingValues(unittest.TestCase):
    def test_adding_some_values(self):
        columns = 2
        rows = 3
        matrix = Matrix(rows, columns)
        matrix.setValue(2, 1, 2)
        matrix.setValue(3, 2, 6)
        self.assertEqual(2, matrix.getValue(2, 1))
        self.assertEqual(6, matrix.getValue(3, 2))

    def test_adding_columns(self):
        columns = 2
        rows = 3
        matrix = Matrix(rows, columns)
        self.assertRaises(ValueError, matrix.setColumn, 1, [1, 2, 3, 4])
        matrix.setColumn(1, [1, 2, 3])
        matrix.setColumn(2, [4, 5, 6])
        self.assertEqual(matrix.matrix, [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(matrix.getColumn(1), [1, 2, 3])

    def test_adding_rows(self):
        columns = 2
        rows = 3
        matrix = Matrix(rows, columns)
        self.assertRaises(ValueError, matrix.setRow, 1, [1, 2, 3])
        matrix.setRow(2, [2, 5])
        self.assertEqual(matrix.getRow(1), [0, 0])
        self.assertEqual(matrix.getRow(2), [2, 5])

if __name__ == "__main__":
    unittest.main()
