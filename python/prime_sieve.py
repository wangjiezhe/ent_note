#!/usr/bin/env python

import sys
import math


def prime_range(n):
    X = [x for x in range(3, n+1) if x % 2 != 0]
    P = [2]

    p = X[0]
    while (p <= math.sqrt(n)):
        P.append(p)
        X = [x for x in X if x % p != 0]
        p = X[0]

    P.extend(X)

    return P


def main():
    if len(sys.argv) == 2:
        print(prime_range(int(sys.argv[1])))


if __name__ == "__main__":
    main()
