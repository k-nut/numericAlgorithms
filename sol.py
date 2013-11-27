#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations


class Polynom:

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __repr__(self):
        rep = []
        for i in range(0, len(self.coefficients)):
            rep.append(str(self.coefficients[i]) + 'x^' + str(i))
        return ' + '.join(rep)

    def calculate_at(self, position):
        sol = 0
        for i in range(0, len(self.coefficients)):
            sol += self.coefficients[i] * position ** i
        return sol


def createPolynomFromNull(nullstellen):
    grad = len(nullstellen) + 1
    coefficients = [0 for stelle in nullstellen]
    coefficients.append(0)
    for i in range(0, grad):
        comb = combinations(nullstellen, i)
        for parts in comb:
            partialProduct = 1
            for part in parts:
                partialProduct *= part
            coefficients[i] += partialProduct
        coefficients[i] *= (-1) ** (grad - i)
    coefficients.reverse()
    for nullstelle in nullstellen:
        assert Polynom(coefficients).calculate_at(nullstelle) == 0

    return Polynom(coefficients)
