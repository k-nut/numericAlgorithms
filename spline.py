#!/usr/bin/python3

from matrix import Matrix

class Spline():
    def __init__(self, xValues, yValues, firstDerivate, lastDerivate):
        assert len(xValues) == len(yValues)

        self.xValues = [float(value) for value in xValues]
        self.yValues = yValues
        self.firstDerivate = firstDerivate
        self.lastDerivate = lastDerivate

        self.length = len(xValues)

        self.calculate_lambdas_and_mys()
        self.calculate_ds()

        self.create_matrix()

    def calculate_lambdas_and_mys(self):
        self.calculate_lambdas()
        self.mys = []
        for i in range(1, self.length - 1):
            self.mys.append(1 - self.lambdas[i -1])
        self.mys.append(1)  # myn is always 1 (capter 3 page 33)

    def calculate_lambdas(self):
        self.lambdas = [1]  # lambda0 is always 1 (capter 3 page 33)
        print(self.length)
        for i in range(1, self.length - 1):
            self.lambdas.append((self.xValues[i + 1] - self.xValues[i]) /
                                (self.xValues[i + 1] - self.xValues[i - 1])
                                )

    def calculate_ds(self):
        xValues = self.xValues
        yValues = self.yValues

        self.ds = []
        self.ds.append(self.calculate_d0())

        for i in range(1, self.length -1):
            firstFraction = 6 / (xValues[i + 1] - xValues[i - 1])

            secondFraction = ((yValues[i + 1] - yValues[i]) /
                              (xValues[i + 1] - xValues[i])
                              )

            thirdFraction = ((yValues[i] - yValues[i - 1]) /
                             (xValues[i] - xValues[i - 1])
                             )

            self.ds.append(firstFraction * (secondFraction - thirdFraction))

        self.ds.append(self.calculate_dn())

    def calculate_d0(self):
        xValues = self.xValues
        yValues = self.yValues
        return 6 / (xValues[1] - xValues[0]) * ((yValues[1] - yValues[0]) /
                                                (xValues[1] - xValues[0])
                                                -self.firstDerivate)

    def calculate_dn(self):
        xValues = self.xValues
        yValues = self.yValues
        return 6 / (xValues[-1] - xValues[-2]) * (self.lastDerivate -
                                                  (yValues[-1] - yValues[-2]) /
                                                  (xValues[-1] - xValues[-2])
                                                  )

    def create_matrix(self):
        self.matrix = Matrix(self.length, self.length)
        print(len(self.lambdas))
        for i in range(1, self.matrix.rowCount + 1):
            self.matrix.setValue(i, i, 2)
        for i in range(1, self.matrix.rowCount):
            self.matrix.setValue(i, i + 1, self.lambdas[i - 1])
        for i in range(2, self.matrix.rowCount + 1):
            self.matrix.setValue(i, i - 1, self.mys[i -2])
            pass
