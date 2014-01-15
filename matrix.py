

class Matrix():
    matrix = []

    def __init__(self, columns, rows):
        self.columnCount = columns
        self.rowCount = rows
        self.setUpMatrix()

    def setUpMatrix(self):
        for row in range(self.rowCount):
            self.matrix.append([0] * self.columnCount)

    def getValue(self, column, row):
        return self.matrix[column - 1][row - 1]
