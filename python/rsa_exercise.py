#!/usr/bin/env python

from sympy.solvers.solvers import solve, Symbol


def get_function(di):
    f = 0
    x = Symbol('x')
    for e, v in di.items():
        f += v * x ** e
    return f


def get_coefficients(n, phi, sigma):
    return {0: -n,
            1: (sigma - phi) / 2 - 1,
            2: n - (sigma + phi) / 2,
            3: 1}


def solve_prob3(n, phi, sigma):
    return solve(get_function(get_coefficients(n, phi, sigma)))


def main3():
    n = 105
    phi = 48
    sigma = 192
    print(solve_prob3(n, phi, sigma))


if __name__ == "__main__":
    main3()
