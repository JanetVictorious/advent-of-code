import os
from collections import deque

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '03.testin'))


def p1(S):
    val = 0
    for s in S:
        idx = int(len(s) / 2)
        s1 = set(s[:idx])
        s2 = set(s[idx:])
        assert len(s[:idx]) == len(s[idx:])
        cmn = s1.intersection(s2)
        if cmn:
            val += D.get(cmn.pop())
    return val


def p2(S):
    val = 0
    d = deque(S)
    while d:
        s1, s2, s3 = d.popleft(), d.popleft(), d.popleft()
        s1, s2, s3 = set(s1), set(s2), set(s3)
        cmn = s1.intersection(s2.intersection(s3))
        if cmn:
            val += D.get(cmn.pop())
    return val


if __name__ == '__main__':
    X = [list(x.strip()) for x in open(FILE_PATH, 'r')]
    lwr_ltr = list(map(chr, range(ord('a'), ord('z')+1)))
    upr_ltr = [i.upper() for i in lwr_ltr]
    L = lwr_ltr + upr_ltr
    D = dict([(l, i+1) for l, i in zip(L, range(len(L)))])
    print(p1(X))
    print(p2(X))
