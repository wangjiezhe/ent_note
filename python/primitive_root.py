#!/usr/bin/env python

import sympy as syp


def primitive_root(p):
    assert syp.isprime(p), "%s is not a prime" % p
    if p == 2:
        return 1
    a = 2
    prime_divisors = syp.primefactors(p-1)

    def test(a):
        for p_i in prime_divisors:
            if pow(a, (p-1)//p_i, p) == 1:
                return False
        return True

    while not test(a):
        a += 1

    return a


def main():
    for p in syp.primerange(1, 20):
        print(p, primitive_root(p))


if __name__ == "__main__":
    main()
