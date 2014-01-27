#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import random
from matrix import Matrix, addedProduct


class TestAddedProduct(unittest.TestCase):
    def testBasicAddedProduct(self):
        list1 = [1, 2, 3]
        list2 = [2, 4, 6]
        self.assertEqual(28, addedProduct(list1, list2))

class TestDecomposition(unittest.TestCase):
    def testLowerDecomposition(self):
        columns = 3
        rows = 3
        matrix = Matrix(rows, columns)
        matrix.setRow(1, [1, 2, 3])
        matrix.setRow(2, [4, 5, 6])
        matrix.setRow(3, [7, 8, 9])
        lu_matrix_list = matrix.get_lu_decomposition()
        new_matrix = lu_matrix_list[0] * lu_matrix_list[1]
        self.assertEqual(matrix.matrix, new_matrix.matrix)


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

    def test_error_handling(self):
        matrix = Matrix(2, 3)
        self.assertRaises(ValueError, matrix.setValue, 0, 1, 3)
        self.assertRaises(ValueError, matrix.setValue, 1, 0, 3)
        self.assertRaises(ValueError, matrix.setValue, 0, 0, 3)
        self.assertRaises(ValueError, matrix.setValue, 3, 1, 3)
        self.assertRaises(ValueError, matrix.setValue, 1, 4, 3)
        self.assertRaises(ValueError, matrix.setValue, 3, 4, 3)


class TestMultiplyingMatrixes(unittest.TestCase):
    def test_multiplying_matrixes(self):
        matrix1 = Matrix(2, 3)
        matrix1.setRow(1, [3, 2, 1])
        matrix1.setRow(2, [1, 0, 2])

        matrix2 = Matrix(3, 2)
        matrix2.setColumn(1, [1, 0, 4])
        matrix2.setColumn(2, [2, 1, 0])

        matrixWithWrongDimension = Matrix(5, 6)

        with self.assertRaises(TypeError):
            matrix2 * matrixWithWrongDimension

        correctMultipliedMatrix = Matrix(2, 2)
        correctMultipliedMatrix.setRow(1, [7, 8])
        correctMultipliedMatrix.setRow(2, [9, 2])
        multipliedMatrix = matrix1 * matrix2
        self.assertEqual(multipliedMatrix.matrix,
                         correctMultipliedMatrix.matrix)

    def test_multiplying_matrixes_with_floats(self):
        matrix1 = Matrix(2, 3)
        matrix1.setRow(1, [3.5, 2, 1])
        matrix1.setRow(2, [1, 0, 2.5])

        matrix2 = Matrix(3, 2)
        matrix2.setColumn(1, [0.5, 0, 4])
        matrix2.setColumn(2, [2, 1.375, 0])

        correctMultipliedMatrix = Matrix(2, 2)
        correctMultipliedMatrix.setRow(1, [5.75, 9.75])
        correctMultipliedMatrix.setRow(2, [10.5, 2])
        multipliedMatrix = matrix1 * matrix2
        self.assertEqual(multipliedMatrix.matrix,
                         correctMultipliedMatrix.matrix)

    def test_multiplying_big_matrixes(self):
        #this only tests speed and not correctness
        matrix1 = Matrix(20, 20)
        matrix2 = Matrix(20, 20)
        for i in range(1, matrix1.rowCount + 1):
            matrix2.setColumn(i, [random.randint(0, 5000) for i in range(20)])
            matrix1.setColumn(i, [random.randint(0, 5000) for i in range(20)])
        matrix1 * matrix2


if __name__ == "__main__":
    unittest.main()
