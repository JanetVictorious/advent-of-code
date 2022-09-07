import os
from collections import Counter

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '07.in'))


_fuel_cache = {}
_fuel_cache[0] = 0
_fuel_cache[1] = 1


def _fuel_sum(n, puzzle=1):
    if puzzle == 1:
        return n
    return sum([v for v in range(n+1)])
    # if n in [0, 1]:
    #     return n
    # if n in _fuel_cache:
    #     return _fuel_cache[n]
    # _fuel_cache[n] = n + _fuel_sum(n-1, puzzle)
    # return _fuel_cache[n]


def p1(cntr, **kwargs):
    start, stop = min(cntr), max(cntr)
    P = {}
    for i in range(start, stop+1):
        P[i] = 0

    idx = 0
    for pos in range(start, stop+1):
        fuel = 0
        for sub in cntr:
            fuel += _fuel_sum(abs(sub-pos), **kwargs) * cntr.get(sub)
        P[idx] += fuel
        idx += 1

    return min(P, key=P.get), min(P.values())


def p2(lst):
    start, stop = min(lst), max(lst)
    P = {}
    for i in range(start, stop+1):
        P[i] = 0


if __name__ == '__main__':
    # Parse input data
    S = open(FILE_PATH, 'r').read()
    X = [int(x) for x in S.split(',')]
    C = Counter([int(x) for x in S.split(',')])

    print(p1(C))
    print(p1(C, puzzle=2))
