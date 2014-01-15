

class Matrix():
    matrix = []

    def __init__(self, columns, rows):
        self.columnCount = columns
        self.rowCount = rows
        self.setUpMatrix()

    def __repr__(self):
        return "\n".join([str(row) for row in self.matrix])

    def setUpMatrix(self):
        for row in range(self.rowCount):
            self.matrix.append([0] * self.columnCount)

    def getValue(self, column, row):
        return self.matrix[column - 1][row - 1]

    """
    def setColumn(self, column, values):
        if len(values) != self.rowCount:
            raise ValueError("The number of values does not equal the number"
                             +"of rows. Should be %i but is %i" % (self.rowCount,
                                                                   len(values)))

        for position, value in enumerate(values):
            self.setValue(position, column, value)
    """

    def setRow(self, row, values):
        if len(values) != self.columnCount:
            raise ValueError("The number of values does not equal the number"
                             +"of columns. Should be %i but is %i" %
                             (self.columnCount, len(values)))

        self.matrix[row - 1] = values

    def setValue(self, column, row, value):
        self.matrix[column - 1][row - 1] = value
