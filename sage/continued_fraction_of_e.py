#!/usr/bin/env sage-python
# coding: utf-8

from __future__ import print_function
# from functools import partial
from functools import wraps
from sage.all import Integer, e, var, symbolic_expression, factorial


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


# series_x = partial(series_z, m0=Integer(1), m1=Integer(3))
# series_y = partial(series_z, m0=Integer(1), m1=Integer(1))


def series_e(m):
    return series_x(m) / series_y(m)


print([series_x(j) for j in range(Integer(10))])
print([series_y(j) for j in range(Integer(10))])
print([series_e(j) for j in range(Integer(10))])
print([series_e(j).n() for j in range(Integer(10))])
print(e.n())


t, n = var('t, n')
__tmp__ = var("t")
G = symbolic_expression(t**n * (t - Integer(1))**n /
                        factorial(n) * e**t).function(t)
__tmp__ = var("n")
T = symbolic_expression(G.integral(t, Integer(0), Integer(1))).function(n)
print([T(j) for j in range(Integer(10))])
