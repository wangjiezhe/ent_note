#!/usr/bin/python

import sys


def egcd(a, b):
    inv = inv_a = inv_b = False
    (a, b) = list(map(int, (a, b)))

    if a < 0:
        inv_a = True
        a = -a

    if b < 0:
        inv_b = True
        b = -b

    if a < b:
        inv = True
        (a, b) = (b, a)

    x = s = 1
    y = r = 0

    while b != 0:
        q = a // b
        c = a % b
        (a, b, r, s, x, y) = (b, c, x-q*r, y-q*s, r, s)
    else:
        g = a

    if inv:
        (x, y) = (y, x)

    if inv_a:
        x = -x

    if inv_b:
        y = -y

    return (g, x, y)


def main():
    if len(sys.argv) == 3:
        print(egcd(sys.argv[1], sys.argv[2]))
    else:
        print("Argument Error!")
        exit(1)


if __name__ == "__main__":
    main()
