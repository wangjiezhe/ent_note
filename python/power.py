#!/usr/bin/env python

from functools import reduce
from egcd import egcd


def binary(m, tolist=False, reverse=False):
    assert isinstance(m, int), "%s is not a integer" % m
    if m < 0:
        m = -m
        inv = True
    else:
        inv = False

    e = []
    while m != 0:
        e.append(m % 2)  # reversed!
        m = m // 2

    if not reverse:
        e = list(reversed(e))

    if tolist:
        if inv:
            e.insert(0, '-')
        return e

    b = reduce(lambda x, y: str(x) + str(y), e)

    if inv:
        b = '-' + b

    return b


def power_mod(a, m, n):
    a, m, n = list(map(int, (a, m, n)))
    if m < 0:
        return inv_mod(power_mod(a, -m, n), n)

    m_l = binary(m, tolist=True, reverse=True)
    # a_l = [a ** 2 ** i % n for i in range(len(m_l))]
    a_l = [a]
    for _ in range(len(m_l)-1):
        a_l.append(pow(a_l[-1], 2, n))

    return reduce(lambda x, y: x * y % n,
                  [i[0] for i in zip(a_l, m_l) if i[1]])


def inv_mod(a, n):
    g, x = egcd(a, n)[:2]
    if g != 1:
        print("Inverse does not exist.")
    else:
        return x


def main1():
    print(binary(100))
    print(binary(-100))
    print(binary(100, tolist=True, reverse=True))
    print(power_mod(7, 91, 100))
    print(power_mod(7, 11, 100))
    print(inv_mod(17, 61))
    print(power_mod(7, -91, 100))
    print(inv_mod(43, 100))


if __name__ == "__main__":
    main1()
