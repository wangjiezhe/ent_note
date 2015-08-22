#!/usr/bin/env sage-python
# coding: utf-8

from __future__ import print_function
from sage.all import Integer, Mod, legendre_symbol, CyclotomicField, CDF, exp,\
    point, pi, I


def kr(a, p):
    if Mod(a, p)**((p - Integer(1)) / Integer(2)) == Integer(1):
        return Integer(1)
    else:
        return -Integer(1)


def main1():
    print("MAIN 1:")
    for a in range(Integer(1), Integer(5)):
        print(a, kr(a, Integer(5)))
    print()


def gauss(a, p):
    v = [(n * a) % p
         for n in range(Integer(1),
                        (p - Integer(1)) // Integer(2) + Integer(1))]
    v = [(x if x < p / Integer(2) else x - p) for x in v]
    v.sort()
    print(v)
    num_neg = len([x for x in v if x < Integer(0)])
    return (-Integer(1))**num_neg


def main2():
    print("MAIN 2:")
    print(gauss(Integer(2), Integer(13)))
    print(legendre_symbol(Integer(2), Integer(13)))
    print(gauss(Integer(2), Integer(31)))
    print(legendre_symbol(Integer(2), Integer(31)))
    print()


def gauss_sum(a, p):
    K = CyclotomicField(p, names=('zeta',))
    (zeta,) = K.gens()
    return sum(legendre_symbol(n, p) * zeta**(a * n)
               for n in range(Integer(1), p))


def main3():
    print("MAIN 3:")
    g2 = gauss_sum(Integer(2), Integer(5))
    print(g2)
    print(g2.complex_embedding())
    print(g2**2)
    print()


def main4():
    print("MAIN 4:")
    zeta = CDF(exp(Integer(2) * pi * I / Integer(5)))
    print(zeta)
    v = [legendre_symbol(n, Integer(5)) * zeta**(Integer(2) * n)
         for n in range(Integer(1), Integer(5))]
    S = sum([point(tuple(z), pointsize=Integer(100)) for z in v])
    G = point(tuple(sum(v)), pointsize=Integer(100), rgbcolor='red')
    (S + G).save(filename="gauss_sum.png")
    print()


def main5():
    print("MAIN 5:")
    print([gauss_sum(a, Integer(7))**Integer(2)
           for a in range(Integer(1), Integer(7))])
    print([gauss_sum(a, Integer(13))**Integer(2)
           for a in range(Integer(1), Integer(13))])
    print()


if __name__ == '__main__':
    main1()
    main2()
    main3()
    main4()
    main5()
