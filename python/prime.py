#!/usr/bin/env python

import random
import numpy as np
import timeit


def is_prime(n):
    assert isinstance(n, int), "%s is not a integer" % n
    if n <= 1:
        return False
    for a in range(1, n):
        if pow(a, n-1, n) != 1:
            return False
    return True


def split_off(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k, n


def is_prime_miller_rabin(n, a=None):
    assert isinstance(n, int), "%s is not a integer" % n
    if n <= 1 or n == 4:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    # k, m = (n-1).val_unit(2)
    k, m = split_off(n-1, 2)
    if not a or a <= 1 or a >= n:
        a = random.randrange(2, n)
    b = pow(a, m, n)
    if b in (1, n-1):
        return True
    for r in range(1, k):
        if pow(b, pow(2, r), n) == n-1:
            return True
    return False


def is_prime_lucas_lehmer(p):
    mer = 2 ** p - 1
    s = np.mod(4, mer)
    for i in range(3, p+1):
        s = np.mod(pow(s, 2, mer) - 2, mer)
        return s == 0


def main1():
    # for n in range(2, 100):
    #     print(n, is_prime(n))
    prime_list = [i for i in range(1, 1000) if is_prime(i)]
    print(len(prime_list), prime_list)
    ti1 = timeit.Timer('[i for i in range(1, 1000) if is_prime(i)]',
                       setup="from __main__ import is_prime")
    ti2 = timeit.Timer('list(filter(is_prime, range(1, 1000)))',
                       setup="from __main__ import is_prime")
    print(ti1.timeit(100))
    print(ti2.timeit(100))


def main2():
    prime_list = [i for i in range(1, 1000) if is_prime_miller_rabin(i, 2)]
    print(len(prime_list), prime_list)
    ti1 = timeit.Timer(
        '[i for i in range(1, 1000) if is_prime_miller_rabin(i)]',
        setup="from __main__ import is_prime_miller_rabin")
    ti2 = timeit.Timer('list(filter(is_prime_miller_rabin, range(1, 1000)))',
                       setup="from __main__ import is_prime_miller_rabin")
    print(ti1.timeit(1000))
    print(ti2.timeit(1000))


def main3():
    strongpseudoprimelist = [i for i in range(1, 10000)
                             if is_prime_miller_rabin(i, 2) and
                             not is_prime(i)]
    print("Strong Pseudoprime: %s" % strongpseudoprimelist)


if __name__ == "__main__":
    # main1()
    # main2()
    main3()
