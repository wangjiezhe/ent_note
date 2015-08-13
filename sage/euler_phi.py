#!/usr/bin/env sage-python

from __future__ import division
from sage.all import *

x = var('x')


def plus(l):
    return reduce(lambda x, y: x+y, l)


def plot1(name, sup=1000):
    P = plot(euler_phi, 2, sup, legend_label="$y=\\varphi(n)$")

    Q = plot(x / 2, 2, sup, rgbcolor='red', legend_label="$y=\\frac{x}{2}$")
    R = plot(x - 1, 2, sup, rgbcolor='red', legend_label="$y=x-1$")

    S = []
    for i in [1, 2]:
        S.append(plot(x / 3 * i, 2, sup, rgbcolor='green',
                      legend_label="$y=\\frac{%sx}{3}$" % i))

    T = []
    for i in [1, 2, 4]:
        T.append(plot(x / 5 * i, 2, sup, rgbcolor='cyan',
                      legend_label="$y=\\frac{%sx}{5}$" % i))

    title_str = "Euler's $\\varphi$-function"

    A = P + Q + R + plus(S) + plus(T)

    A.save(filename=name, figsize=[16, 9],
           axes_labels=['$x$', '$y$'], title=title_str)


def plot2(name):
    P = plot(euler_phi, 2, 100000, legend_label="$y=\\varphi(n)$")
    Q = plot(x / 5, 2, 100000, rgbcolor='red', legend_label="$y=\\frac{x}{5}$")

    title_str = "Euler's $\\varphi$-function"

    A = P + Q

    A.save(filename=name, figsize=[16, 9],
           axes_labels=['$x$', '$y$'], title=title_str)


def plot3(name, sup=1000):
    def f(x):
        return euler_phi(x) / x

    P = list_plot([(x, f(x)) for x in range(2, sup+1)])

    Q = []
    for i in [1/5, 2/5, 4/5]:
        Q.append(plot(i, 2, sup, rgbcolor='cyan'))

    R = []
    for i in [1/3, 2/3]:
        R.append(plot(i, 2, sup, rgbcolor='green'))

    S = []
    for i in [1/2, 1]:
        S.append(plot(i, 2, sup, rgbcolor='red'))

    A = P + plus(Q) + plus(R) + plus(S)

    title_str = "$y=\\frac{\\varphi(n)}{n}$"

    A.save(filename=name, figsize=[16, 9],
           axes_labels=['$x$', '$y$'], title=title_str)


if __name__ == "__main__":
    plot1("plot1_0.png")
    plot1("plot1_1.png", 10000)
    plot1("plot1_2.png", 100000)
    # plot2("plot2.png")
    # plot3("plot3_0.png")
    # plot3("plot3_1.png", 10000)
    # plot3("plot3_2.png", 100000)
    # plot3("plot3_2.png", 1000000)
    # plot3("plot3_2.png", 10000000)
