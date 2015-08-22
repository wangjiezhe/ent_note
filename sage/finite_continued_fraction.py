#!/usr/bin/env sage-python
# coding: utf-8

from __future__ import print_function
from sage.all import Integer, continued_fraction, continued_fraction_list,\
    CFF, pi, e, point, line


def main1():
    print(continued_fraction(Integer(17) / Integer(23)))
    print(continued_fraction(e))
    print(continued_fraction_list(e, bits=21))
    print(continued_fraction_list(e, bits=30))


def main2():
    a = continued_fraction(Integer(17) / Integer(23))
    print(a)
    b = continued_fraction(Integer(6) / Integer(23))
    print(b)
    A = CFF(a)
    B = CFF(b)
    print(A + B)
    print(A.value())
    print(a.value())


def main3():
    c = continued_fraction(pi)
    print(c.convergents()[:6].list())


def main4():
    c = continued_fraction(pi)
    for n in range(-1, 13):
        print(c.p(n) * c.q(n - Integer(1)) -
              c.q(n) * c.p(n - Integer(1)), end=' ')
    print()
    for n in range(Integer(13)):
        print(c.p(n) * c.q(n - Integer(2)) -
              c.q(n) * c.p(n - Integer(2)), end=' ')
    print()


def main5():
    c = continued_fraction(
        [Integer(1), Integer(2), Integer(3), Integer(4), Integer(5)])
    print(c)
    print(c.convergents())
    print([c.p(n) for n in range(c.length())])
    print([c.q(n) for n in range(c.length())])


def main6():
    c = continued_fraction([Integer(1)] * (8))
    v = [(i, c.p(i) / c.q(i)) for i in range(c.length())]
    P = point(v, rgbcolor=(0, 0, 1), pointsize=40)
    L = line(v, rgbcolor=(0.5, 0.5, 0.5))
    L2 = line([(Integer(0), c.value()), (c.length() - Integer(1), c.value())],
              thickness=0.5, rgbcolor=(0.7, 0, 0))
    (L + L2 + P).save(filename="continued_fraction.png")
    print("Graph is saved as continued_fraction.png")


if __name__ == "__main__":
    main_list = [m for m in dir() if m[:4] == 'main']
    for m in main_list:
        print(m + ':')
        eval(m + '()')
        print()
