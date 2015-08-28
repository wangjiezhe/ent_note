#!/usr/bin/env python
# coding: utf-8

from functools import wraps, partial
from timeit import timeit
from numpy import exp
from scipy.special import factorial
from scipy.integrate import quad


def cache(func):
    caches = {}

    @wraps(func)
    def _cache(*args, **kw):
        key = str(func) + str(args)
        if key in caches:
            return caches[key]
        result = func(*args, **kw)
        caches[key] = result
        return caches[key]

    return _cache


@cache
def series_z(m, m0, m1):
    if m == 0:
        return m0
    elif m == 1:
        return m1
    else:
        return (2 * (2 * m - 1) *
                series_z(m - 1, m0, m1) +
                series_z(m - 2, m0, m1))


def series_x(m):
    return series_z(m, 1, 3)


def series_y(m):
    return series_z(m, 1, 1)


def series_e(m):
    return series_x(m) / series_y(m)


def series_z_nocache(m, m0, m1):
    if m == 0:
        return m0
    elif m == 1:
        return m1
    else:
        return (2 * (2 * m - 1) *
                series_z(m - 1, m0, m1) +
                series_z(m - 2, m0, m1))


series_x_nocache = partial(series_z_nocache, m0=1, m1=3)
series_y_nocache = partial(series_z_nocache, m0=1, m1=1)


def series_e_nocache(m):
    return series_x_nocache(m) / series_y_nocache(m)


def main1():
    print([series_x(j) for j in range(10)])
    print([series_y(j) for j in range(10)])
    print([series_e(j) for j in range(10)])
    print([series_e(j) for j in range(10)])
    print(exp(1))


def main2():
    def G(t, n):
        return t**n * (t - 1)**n / factorial(n) * exp(t)
    print([quad(G, 0, 1, args=(n,))[0] for n in range(10)])


def main3():
    print(timeit('[series_x(k) for k in range(1000)]',
                 setup='from __main__ import series_x', number=100))
    print(timeit('[series_y(k) for k in range(1000)]',
                 setup='from __main__ import series_y', number=100))
    print(timeit('[series_e(k) for k in range(1000)]',
                 setup='from __main__ import series_e', number=100))
    print(timeit('[series_x_nocache(k) for k in range(1000)]',
                 setup='from __main__ import series_x_nocache', number=100))
    print(timeit('[series_y_nocache(k) for k in range(1000)]',
                 setup='from __main__ import series_y_nocache', number=100))
    print(timeit('[series_e_nocache(k) for k in range(1000)]',
                 setup='from __main__ import series_e_nocache', number=100))


if __name__ == "__main__":
    main_list = [main for main in dir() if main[:4] == 'main']
    for main in main_list:
        print(main + ':')
        eval(main + '()')
        print()
