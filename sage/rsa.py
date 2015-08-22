#!/usr/bin/env sage-python

from __future__ import division, print_function
from sage.all import next_prime, gcd, Mod, lift, sqrt, ceil, round, is_odd,\
    ZZ, QQ, Integer, randrange, factor, set_random_seed, qsieve


def rsa(bits):
    # only prove correctness up to 1024bits
    proof = (bits <= 1024)
    p = next_prime(ZZ.random_element(2**(bits // 2 + 1)),
                   proof=proof)
    q = next_prime(ZZ.random_element(2**(bits // 2 + 1)),
                   proof=proof)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    while True:
        e = ZZ.random_element(1, phi_n)
        if gcd(e, phi_n) == 1:
            break
    d = lift(Mod(e, phi_n)**(-1))
    return e, d, n


def encrypt(m, e, n):
    return lift(Mod(m, n)**e)


def decrypt(c, d, n):
    return lift(Mod(c, n)**d)


def encode(s):
    s = str(s)
    # return sum(ord(s[i])*256**i for i in range(len(s)))
    return sum(ord(s[i]) << (8 * i) for i in range(len(s)))


def decode(n):
    n = Integer(n)
    v = []
    while n != 0:
        # v.append(chr(n % 256))
        v.append(chr(n & 255))
        # n //= 256
        n >>= 8
    return ''.join(v)


def crack_rsa(n, phi_n):
    # R = PolynomialRing(QQ, 'x')
    # x = R.gen()
    x = QQ['x'].gen()
    f = x ** 2 - (n + 1 - phi_n) * x + n
    return [b for b, _ in f.roots()]


def crack_when_pq_close(n):
    t = Integer(ceil(sqrt(n)))
    while True:
        k = t**2 - n
        if k > 0:
            s = Integer(int(round(sqrt(t**2 - n))))
            if s**2 + n == t**2:
                return t + s, t - s
        t += 1


def crack_given_decrypt(n, m):
    n = Integer(n)
    m = Integer(m)

    while True:
        if is_odd(m):
            break
        divide_out = True
        for _ in range(5):
            a = randrange(1, n)
            if gcd(a, n) == 1:
                if Mod(a, n) ** (m // 2) != 1:
                    divide_out = False
                    break
        if divide_out:
            m //= 2
        else:
            break

    while True:
        a = randrange(1, n)
        g = gcd(lift(Mod(a, n) ** (m // 2)) - 1, n)
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
    p = next_prime(2**128)
    print(p)
    q = next_prime(p)
    print(q)
    print(crack_when_pq_close(p * q))


def main5():
    n = 32295194023343
    e = 29468811804857
    d = 11127763319273
    print(crack_given_decrypt(n, e * d - 1))
    print(factor(n))


def main6():
    e = 22601762315966221465875845336488389513
    d = 31940292321834506197902778067109010093
    n = 268494924039590992469444675130990465673
    p = crack_given_decrypt(n, e * d - 1)
    print(p)
    print(n % p)


def main7():
    set_random_seed(0)
    p = next_prime(randrange(2**96))
    q = next_prime(randrange(2**97))
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
