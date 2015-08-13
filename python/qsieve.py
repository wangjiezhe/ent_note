#!/usr/bin/env python

import os


def qsieve(n):
    n = int(n)
    if len(str(n)) < 40:
        raise ValueError("n must have at least 40 digits")
    qs = "QuadraticSieve"

    if os.system('type %s >/dev/null 2>&1' % qs) != 0:
        raise NameError("Command %s not found,\
please install it in your system" % qs)

    out = os.popen('echo "%s" | %s 2>&1' % (n, qs)).read()
    fac_str = 'FACTORS:'
    i = out.find(fac_str)
    if i == -1:
        return []
    else:
        out = out[i+len(fac_str)+1:].strip()
        v = out.split()
        v = sorted(set(int(m) for m in v if int(m) != n))
        return v
