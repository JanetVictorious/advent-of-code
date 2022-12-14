import os
import numpy as np
from collections import deque

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '12.in'))

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]


def p1(S, part=1):
    Q = deque()
    for r in range(NR):
        for c in range(NC):
            if (r, c) == START and part == 1:
                Q.append((0, (r, c)))
            elif ((r, c) == START or S[r, c] == 1) and part == 2:
                Q.append((0, (r, c)))

    Z = set()
    while Q:
        d, (r, c) = Q.popleft()
        if (r, c) in Z:
            continue
        Z.add((r, c))
        if (r, c) == END:
            return d
        for i in range(4):
            r2 = r + DR[i]
            c2 = c + DC[i]
            if 0 <= r2 < NR and 0 <= c2 < NC and S[r2, c2] <= S[r, c] + 1:
                Q.append((d + 1, (r2, c2)))
    return None


if __name__ == '__main__':
    X = [list(x.strip()) for x in open(FILE_PATH, 'r')]
    lwr_ltr = list(map(chr, range(ord('a'), ord('z')+1)))
    L = dict()
    for idx, val in enumerate(lwr_ltr):
        L[val] = idx + 1
    NR = len(X)
    NC = len(X[0])
    XS = np.zeros((NR, NC))
    for i in range(NR):
        for j in range(NC):
            val = X[i][j]
            if val == 'S':
                XS[i, j] = 0
                START = (i, j)
            elif val == 'E':
                XS[i, j] = L['z'] + 1
                END = (i, j)
            else:
                XS[i, j] = L[val]
    print(p1(XS))
    print(p1(XS, part=2))
