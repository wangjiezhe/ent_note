#!/usr/bin/env python

from sympy.ntheory import nextprime, factorint
from sympy.polys import gcd, gcdex
from sympy.functions import sqrt, ceiling
from sympy.solvers.solvers import solve, Symbol
from random import randrange, seed
from qsieve import qsieve


def inv_mod(a, n):
    x, g = gcdex(n, a)[1:]
    if g == 1:
        return int(x) if x > 0 else int(n - x)
    else:
        raise ValueError("Inverse does not exist.")


def rsa(bits):
    p = nextprime(randrange(2**(bits // 2 + 1)))
    q = nextprime(randrange(2**(bits // 2 + 1)))
    n = p * q
    phi_n = (p - 1) * (q - 1)
    while True:
        e = randrange(1, phi_n)
        if gcd(e, phi_n) == 1:
            break
    d = inv_mod(e, phi_n)
    return e, d, n


def encrypt(m, e, n):
    return pow(m, e, n)


def decrypt(c, d, n):
    return pow(c, d, n)


def encode(s):
    s = str(s)
    # return sum(ord(s[i])*256**i for i in range(len(s)))
    return sum(ord(s[i]) << (8 * i) for i in range(len(s)))


def decode(n):
    n = int(n)
    v = []
    while n != 0:
        # v.append(chr(n % 256))
        v.append(chr(n & 255))
        # n //= 256
        n >>= 8
    return ''.join(v)


def crack_rsa(n, phi_n):
    x = Symbol('x')
    f = x ** 2 - (n + 1 - phi_n) * x + n
    return solve(f)


def crack_when_pq_close(n):
    t = ceiling(sqrt(n))
    while True:
        k = t**2 - n
        if k > 0:
            s = round(int(sqrt(t**2 - n)))
            if s**2 + n == t**2:
                return t + s, t - s
        t += 1


def crack_given_decrypt(n, m):
    n = int(n)
    m = int(m)

    while True:
        if m % 2 != 0:
            break
        divide_out = True
        for _ in range(5):
            a = randrange(1, n)
            if gcd(a, n) == 1:
                if pow(a, m // 2, n) != 1:
                    divide_out = False
                    break
        if divide_out:
            m //= 2
        else:
            break

    while True:
        a = randrange(1, n)
        g = gcd(pow(a, m // 2, n) - 1, n)
        if g != 1 and g != n:
            return g


def main1():
    e, d, n = rsa(20)
    print(e, d, n)
    c = encrypt(123, e, n)
    print("123 -> %s" % c)
    print(decrypt(c, d, n))


def main2():
    m = encode('Run Nikita!')
    print(m)
    print(decode(m))


def main3():
    print(crack_rsa(31615577110997599711, 31615577098574867424))


def main4():
    print(crack_when_pq_close(23360947609))
    p = nextprime(2**128)
    print(p)
    q = nextprime(p)
    print(q)
    print(crack_when_pq_close(p * q))


def main5():
    n = 32295194023343
    e = 29468811804857
    d = 11127763319273
    print(crack_given_decrypt(n, e * d - 1))
    print(factorint(n))


def main6():
    e = 22601762315966221465875845336488389513
    d = 31940292321834506197902778067109010093
    n = 268494924039590992469444675130990465673
    p = crack_given_decrypt(n, e * d - 1)
    print(p)
    print(n % p)


def main7():
    seed(0)
    p = nextprime(randrange(2**96))
    q = nextprime(randrange(2**97))
    n = p * q
    print(p, q, n)
    print(qsieve(n))


if __name__ == "__main__":
    main1()
    main2()
    main3()
    main4()
    main5()
    main6()
    main7()
