#!/usr/bin/python3


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
        pass
