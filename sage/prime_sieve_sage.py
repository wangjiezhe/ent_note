#!/usr/bin/env sage-python

from __future__ import print_function
import sys
from sage.all import is_odd, sqrt, sage_eval


def prime_range(n):
    X = [x for x in range(3, n+1) if is_odd(x)]
    P = [2]

    p = X[0]
    while p <= sqrt(n):
        P.append(p)
        X = [x for x in X if x % p != 0]
        p = X[0]

    P.extend(X)

    return P


def main():
    if len(sys.argv) == 2:
        print(prime_range(sage_eval(sys.argv[1])))


if __name__ == "__main__":
    main()
