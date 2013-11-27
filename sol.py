#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations


class Polynom:

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __repr__(self):
        rep = []
        for index, coefficient in enumerate(self.coefficients):
            rep.append("%ix^%i" % (coefficient, index))
        return ' + '.join(rep)

    def calculate_at(self, position):
        sol = 0
        for index, coefficient in enumerate(self.coefficients):
            sol += coefficient * position ** index
        return sol


def createPolynomFromNull(nullstellen):
    grad = len(nullstellen) + 1
    coefficients = [0 for pos in range(0, len(nullstellen) + 1)]
    for i in range(0, grad):
        comb = combinations(nullstellen, i)
        for parts in comb:
            coefficients[i] += product(parts)
        coefficients[i] *= (-1) ** (grad - i)
    coefficients.reverse()
    for nullstelle in nullstellen:
        assert Polynom(coefficients).calculate_at(nullstelle) == 0

    return Polynom(coefficients)


def product(collection):
    product = 1
    for element in collection:
        product *= element
    return product
