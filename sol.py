#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations


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
            newCoefficients = self.coefficients
            for i in range(0, summand_grad):
                newCoefficients[i] += summand.coefficients[i]
        else:
            newCoefficients = summand.coefficients
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
        comb = combinations(nullstellen, i)
        for parts in comb:
            coefficients[i] += product(parts)

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
    firstValues = allValues[0]

    while len(allValues[-1]) > 1:
        flastValues = allValues[-1]

        newValues = [0 for x in range(0, len(flastValues) -1)]
        c = len(newValues) - 1
        s = len(firstValues) -1
        for x in range(len(flastValues) - 1, 0, -1):
            newValues[x - 1] = float((flastValues[x] - flastValues[x - 1])) / (firstValues[s] - firstValues[c])
            c -= 1
            s -= 1
        allValues.append(newValues)

    finalPolynomCoefficients = []  # c0, c1, c2 etc
    for l in allValues[1:]:
        finalPolynomCoefficients.append(l[0])
    print finalPolynomCoefficients

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


def product(collection):
    product = 1
    for element in collection:
        product *= element
    return product

if __name__ == "__main__":
    pol = newton([1, 3, 5], [3, 7, 14])
    print(pol)

    pol2 = newton([-2, -1, 0, 1, 2, 3], [-16, 0, 4, 8, 0, 64])
    print(pol2)
