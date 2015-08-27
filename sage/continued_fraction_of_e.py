#!/usr/bin/env sage-python
# coding: utf-8

from __future__ import print_function
from functools import wraps, partial
from sage.all import Integer, e, var, symbolic_expression, factorial, timeit


def cache(func):
    caches = {}

    @wraps(func)
    def _cache(*args, **kw):
        key = func.func_name + str(args)
        if key in caches:
            return caches[key]
        result = func(*args, **kw)
        caches[key] = result
        return caches[key]

    return _cache


@cache
def series_z(m, m0, m1):
    if m == Integer(0):
        return m0
    elif m == Integer(1):
        return m1
    else:
        return (Integer(2) * (Integer(2) * m - Integer(1)) *
                series_z(m - Integer(1), m0, m1) +
                series_z(m - Integer(2), m0, m1))


def series_x(m):
    return series_z(m, Integer(1), Integer(3))


def series_y(m):
    return series_z(m, Integer(1), Integer(1))


def series_e(m):
    return series_x(m) / series_y(m)


def series_z_nocache(m, m0, m1):
    if m == Integer(0):
        return m0
    elif m == Integer(1):
        return m1
    else:
        return (Integer(2) * (Integer(2) * m - Integer(1)) *
                series_z(m - Integer(1), m0, m1) +
                series_z(m - Integer(2), m0, m1))


series_x_nocache = partial(series_z_nocache, m0=Integer(1), m1=Integer(3))
series_y_nocache = partial(series_z_nocache, m0=Integer(1), m1=Integer(1))


def series_e_nocache(m):
    return series_x_nocache(m) / series_y_nocache(m)


def main1():
    print([series_x(j) for j in range(Integer(10))])
    print([series_y(j) for j in range(Integer(10))])
    print([series_e(j) for j in range(Integer(10))])
    print([series_e(j).n() for j in range(Integer(10))])
    print(e.n())


def main2():
    t, n = var('t, n')
    G = symbolic_expression(t**n * (t - Integer(1))**n /
                            factorial(n) * e**t).function(t)
    T = symbolic_expression(G.integral(t, Integer(0), Integer(1))).function(n)
    print([T(j) for j in range(Integer(10))])
    print([T(j).n() for j in range(Integer(10))])


def main3():
    timeit('series_x(Integer(100))')
    timeit('series_y(Integer(100))')
    timeit('series_e(Integer(100))')
    timeit('series_x_nocache(Integer(100))')
    timeit('series_y_nocache(Integer(100))')
    timeit('series_e_nocache(Integer(100))')


if __name__ == "__main__":
    main_list = [main for main in dir() if main[:4] == 'main']
    for main in main_list:
        print(main + ':')
        eval(main + '()')
        print()
