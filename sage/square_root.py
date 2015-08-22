#!/usr/bin/env sage-python
# coding: utf-8

from __future__ import print_function
from sage.all import PolynomialRing, GF, Integer, legendre_symbol


def main1():
    S = PolynomialRing(GF(Integer(13)), names=('x',))
    (x,) = S.gens()
    R = S.quotient(x**Integer(2) - Integer(3), names=('alpha',))
    (alpha,) = R.gens()
    print((Integer(2) + Integer(3) * alpha)
          * (Integer(1) + Integer(2) * alpha))


def find_sqrt(a, p):
    assert (p - Integer(1)) % Integer(4) == Integer(0)
    assert legendre_symbol(a, p) == Integer(1)

    S = PolynomialRing(GF(p), names=('x',))
    (x,) = S.gens()
    R = S.quotient(x**Integer(2) - a, names=('alpha',))
    (alpha,) = R.gens()

    while True:
        z = GF(p).random_element()
        w = (Integer(1) + z * alpha)**((p - Integer(1)) // Integer(2))
        (u, v) = (w[Integer(0)], w[Integer(1)])
        if v != Integer(0):
            break

    if (-u / v)**Integer(2) == a:
        return -u / v
    if ((Integer(1) - u) / v)**Integer(2) == a:
        return (Integer(1) - u) / v
    if ((-Integer(1) - u) / v)**Integer(2) == a:
        return (-Integer(1) - u) / v


def main2():
    for _ in range(10):
        b = find_sqrt(Integer(3), Integer(13))
        print(b, b**2)

    for _ in range(10):
        print(find_sqrt(Integer(5), Integer(389)))


if __name__ == '__main__':
    main1()
    main2()
