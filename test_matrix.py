#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from matrix import Matrix, addedProduct


class TestAddedProduct(unittest.TestCase):
    def testBasicAddedProduct(self):
        list1 = [1, 2, 3]
        list2 = [2, 4, 6]
        self.assertEqual(28, addedProduct(list1, list2))


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


class TestMultiplyingMatrixes(unittest.TestCase):
    def test_multiplying_empty_matrixes(self):
        matrix1 = Matrix(2, 3)
        matrix1.setRow(1, [3, 2, 1])
        matrix1.setRow(2, [1, 0, 2])

        matrix2 = Matrix(3, 2)
        matrix2.setColumn(1, [1, 0, 4])
        matrix2.setColumn(2, [2, 1, 0])

        matrixWithWrongDimension = Matrix(5, 6)

        with self.assertRaises(TypeError):
            matrix2 * matrixWithWrongDimension

        print("Matrix 1")
        print(matrix1)
        print("Matrix 2")
        print(matrix2)
        correctMultipliedMatrix = Matrix(2, 2)
        correctMultipliedMatrix.setRow(1, [7, 8])
        correctMultipliedMatrix.setRow(2, [9, 2])
        multipliedMatrix = matrix1 * matrix2
        self.assertEqual(multipliedMatrix.matrix,
                correctMultipliedMatrix.matrix)



if __name__ == "__main__":
    unittest.main()
