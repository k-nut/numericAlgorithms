#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Polynom:

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __repr__(self):
        rep = []
        for index, coefficient in enumerate(self.coefficients):
            rep.append("%sx^%i" % (str(coefficient), index))
        return ' + '.join(rep)

    def calculate_at(self, position):
        sol = 0
        for index, coefficient in enumerate(self.coefficients):
            sol += coefficient * position ** index
        return sol

    def __add__(self, summand):
        own_grad = len(self.coefficients)
        summand_grad = len(summand.coefficients)
        if own_grad > summand_grad:
            newCoefficients = list(self.coefficients)
            for i in range(0, summand_grad):
                newCoefficients[i] += summand.coefficients[i]
        else:
            newCoefficients = list(summand.coefficients)
            for i in range(0, own_grad):
                newCoefficients[i] += self.coefficients[i]
        return Polynom(newCoefficients)

    def __mul__(self, number):
        coefficients = [number * float(coefficient) for coefficient in self.coefficients]
        return Polynom(coefficients)


def createPolynomFromNull(nullstellen):
    grad = len(nullstellen) + 1
    coefficients = [0 for pos in range(0, len(nullstellen) + 1)]
    for i in range(0, grad):
        comb = combinate(nullstellen, i)
        for parts in comb:
            coefficients[i] += product(parts)
        #coefficients[i] *= (-1) ** (grad - 1 - i)

    multiplier = 1
    for i in range(0, grad):
        coefficients[i] *= multiplier
        multiplier *= -1

    coefficients.reverse()

    for nullstelle in nullstellen:
        assert Polynom(coefficients).calculate_at(nullstelle) == 0

    return Polynom(coefficients)


def newton(xValues, yValues):
    allValues = []
    allValues.append(xValues)
    allValues.append(yValues)

    while len(allValues[-1]) > 1:
        flastValues = allValues[-1]

        newValues = [0 for x in range(0, len(flastValues) -1)]
        c = len(newValues) - 1
        s = len(xValues) -1
        for x in range(len(flastValues) - 1, 0, -1):
            newValues[x - 1] = float((flastValues[x] - flastValues[x - 1])) / (xValues[s] - xValues[c])
            c -= 1
            s -= 1
        allValues.append(newValues)

    finalPolynomCoefficients = [value[0] for value in allValues[1:]]  # c0, c1, c2 etc

    polynoms = []  # n0, n1, n2 etc
    polynoms.append(Polynom([1]))   # n0 is allways 1
    for i in range(1, len(xValues)):
        upTo = xValues[:i]
        polynoms.append(createPolynomFromNull(upTo))

    for i in range(0, len(polynoms)):
        polynoms[i] = polynoms[i] * finalPolynomCoefficients[i]

    finalPolynom = polynoms[0]
    for i in range(1, len(polynoms)):
        finalPolynom = finalPolynom + polynoms[i]

    for i in range(0, len(xValues)):
        assert yValues[i] == finalPolynom.calculate_at(xValues[i])

    return finalPolynom


def lagrange(xValues, yValues):
    starValues = []
    starPolynoms = []
    for x in xValues:
        copy = list(xValues)
        copy.remove(x)
        pol = createPolynomFromNull(copy)
        starPolynoms.append(pol)
        sol = pol.calculate_at(x)
        starValues.append(sol)

    polynoms = []

    for i in range(0, len(starValues)):
        polynoms.append(starPolynoms[i] * (1.0 / float(starValues[i]) * yValues[i]))

    finalPolynom = polynoms[0]
    for i in range(1, len(polynoms)):
        finalPolynom += polynoms[i]

    return finalPolynom


def product(collection):
    product = 1
    for element in collection:
        product *= element
    return product


def combinate(inputValues, k):

    del returnValues[:]
    del combinationValues[:]

    if k == 0:
        yield [1]
        raise StopIteration

    for i in range(0, k):
        combinationValues.append(0)

    combinations2(inputValues, len(inputValues), k)

    for x in returnValues:
        yield x


def combinations2(inputValues, n, k):
    global combinationValues

    if n > k:
        combinations2(inputValues, n - 1, k)

    if n >= k:
        k -= 1
        combinationValues[k] = inputValues[n - 1]
        if k > 0:
            combinations2(inputValues, n - 1, k)
        else:
            rep = []
            for value in combinationValues:
                rep.append(value)

            returnValues.append(rep)


combinationValues = []
returnValues = []

if __name__ == "__main__":
    #pol = newton([1, 3, 5], [3, 7, 14])
    #print(pol)

    #pol2 = newton([-2, -1, 0, 1, 2, 3], [-16, 0, 4, 8, 0, 64])
    #print(pol2)

    # lagrange_pol = lagrange([1, 3, 5], [3, 7, 14])
    # print("\nMAIN")
    # print(lagrange_pol)
    # print(lagrange_pol.coefficients)
    polynom1 = createPolynomFromNull([1, 2, 3])

    inputValues = [1]
    combinate(inputValues, 3)
    #
    # inputValues = [1, 2, 3, 4, 6, 9]
    # combinate(inputValues, 3)
