

class Matrix():

    def __init__(self, rows, columns):
        self.columnCount = columns
        self.rowCount = rows
        self.matrix = []
        self.setUpMatrix()

    def __repr__(self):
        return "\n".join([str(row) for row in self.matrix])

    def __mul__(self, multipliedMatrix):
        if (self.columnCount != multipliedMatrix.rowCount):
            raise TypeError("Number of row and column have to match")
        newMatrix = Matrix(self.rowCount, multipliedMatrix.columnCount)
        for columnNumber in range(1, newMatrix.columnCount + 1):
            for rowNumber in range(1, newMatrix.rowCount + 1):
                row = self.getRow(rowNumber)
                column = multipliedMatrix.getColumn(columnNumber)
                newMatrix.setValue(rowNumber,
                                   columnNumber,
                                   addedProduct(row, column)
                                   )
        return newMatrix

    def setUpMatrix(self):
        for row in range(self.rowCount):
            self.matrix.append([0] * self.columnCount)

    def getValue(self, row, column):
        return self.matrix[row - 1][column - 1]

    def setColumn(self, column, values):
        if len(values) != self.rowCount:
            raise ValueError("The number of values does not equal the number"
                             +"of rows. Should be %i but is %i" % (self.rowCount,
                                                                   len(values)))

        for position, value in enumerate(values):
            self.setValue(position + 1, column, value)

    def getColumn(self, columnNumber):
        column = []
        for row in range(1, self.rowCount + 1):
            column.append(self.getValue(row, columnNumber))
        return column

    def getRow(self, rowNumber):
        row = []
        for column in range(1, self.columnCount + 1):
            row.append(self.getValue(rowNumber, column))
        return row

    def setRow(self, row, values):
        if len(values) != self.columnCount:
            raise ValueError("The number of values does not equal the number"
                             +"of columns. Should be %i but is %i" %
                             (self.columnCount, len(values)))

        for position, value in enumerate(values):
            self.setValue(row, position + 1, value)

    def setValue(self, row, column, value):
        if row > self.rowCount or column > self.columnCount:
            raise ValueError("Row or column value to high for the matrix")
        if row < 1 or column < 1:
            raise ValueError("Row and column must be at least 1")
        self.matrix[row - 1][column - 1] = value


    def get_lu_decomposition(self):
        upper_matrix = Matrix(self.rowCount, self.columnCount)
        for row in range(1, self.rowCount+1):
            upper_matrix.setValue(row, row, 1)

        lower_matrix = Matrix(self.rowCount, self.columnCount)
        for row in range(1, self.rowCount+1):
            lower_matrix.setRow(row, self.getRow(row))

        for column in range(1, self.columnCount):
            for row in range(column + 1, self.rowCount+1):
                multiplier = lower_matrix.getRow(row)[column-1] / lower_matrix.getRow(column)[column-1]
                upper_matrix.setValue(row, column, multiplier)
                for i in range(1, self.columnCount + 1):
                    lower_matrix.setValue(row, i, lower_matrix.getValue(row, i) - multiplier * lower_matrix.getValue(column, i))

        return_values = []
        return_values.append(upper_matrix)
        return_values.append(lower_matrix)
        return return_values;

def addedProduct(enumerable1, enumerable2):
    assert len(enumerable1) == len(enumerable2)
    product = 0
    for i, element in enumerate(enumerable1):
        product += element * enumerable2[i]
    return product


