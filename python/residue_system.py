#!/usr/bin/env python

from sympy.ntheory import factorint
from sympy.polys import gcd
from functools import reduce


def get_tuple_list(l):
    """
    @type l: list
    @rtype: list of tuple

    @return: all possible 2-tuple made from elements in l,
             regardless of the order
    """
    l = list(set(l))
    # l = list({}.fromkeys(l).keys())
    assert len(l) > 1
    if len(l) == 2:
        return [tuple(l)]
    else:
        rel = [(l[0], x) for x in l[1:]]
        rel.extend(get_tuple_list(l[1:]))
        return rel


def is_coprime_list(l):
    """
    @type l: list of integer > 0
    @rtype: bool

    @return: if every two elements in l are coprime
    """
    l = get_tuple_list(l)
    if max(map(gcd, l)) == 1:
        return True
    else:
        return False


def crs_simple(n):
    """
    @type n: integer > 0
    @rtype: list

    @return: a complete residue system modulo n
    """
    return list(range(n))


def rrs_simple(n):
    """
    @type n: integer > 0
    @rtype: list

    @return: a reduced residue system modulo n
    """
    return [x for x in range(n) if gcd(x, n) == 1]


def rrs_of_prime_power(p, k):
    """
    @type p: prime
    @type k: integer > 0
    @rtype: list

    @return: a reduced residue system modulo p**k
    """
    if k == 1:
        return range(1, p)
    else:
        return [a+b*p for a in range(1, p) for b in range(p**(k-1))]
        # return [x for x in range(1, pow(p, k) if x % p != 0]


def rrs_of_prime_power_t(p, k, res_t=0):
    if res_t == 1:
        pass
    elif res_t == 2:
        pass
    else:
        pass


def residue_system(n, reduced=False, mod=True):
    """
    @type n: integer > 1
    @type reduced: bool
    @param reduced: return a reduced residue system modulo n or
                    a complete residue system modulo n
    @type mod: bool
    @param mod: use mod when generate final list or not
    @rtype: list

    @return: a residue system modulo n
    """
    assert isinstance(n, int) and n > 1

    if n == 2:
        return [1] if reduced else [0, 1]

    n_fact = factorint(n)

    # if len(n_fact) == 1:
    #     if reduced:
    #         return rrs_of_prime_power(
    #             *list(n_fact.items())[0])
    #     else:
    #         return list(range(n))

    m_list = [pow(*e) for e in n_fact.items()]
    M_list = [n//x for x in m_list]

    if reduced:
        vec = [rrs_of_prime_power(*e)
               for e in n_fact.items()]
    else:
        vec = [list(range(x)) for x in m_list]

    vec = [[x*s for x in l] for l, s in zip(vec, M_list)]

    if mod:
        res = reduce(lambda l1, l2: [(x+y) % n for x in l1 for y in l2],
                     vec)
    else:
        res = reduce(lambda l1, l2: [x+y for x in l1 for y in l2],
                     vec)

    res.sort()

    return res
