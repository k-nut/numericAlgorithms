

class Matrix():

    def __init__(self, rows, columns):
        self.columnCount = columns
        self.rowCount = rows
        self.matrix = []
        self.setUpMatrix()

    def __repr__(self):
        return "\n".join([str(row) for row in self.matrix])

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
        self.matrix[row - 1][column - 1] = value
