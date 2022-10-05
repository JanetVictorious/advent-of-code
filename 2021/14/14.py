import os
from collections import Counter, deque

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '14.in'))


def p1(m, c, iter: int = 40):
    diff10, diff40 = 0, 0
    for i in range(iter):
        Y = Counter()
        for j in c:
            Y[j[0] + m[j]] += c[j]
            Y[m[j] + j[1]] += c[j]
        c = Y
        if i in [9, 39]:
            CF = Counter()
            for k in c:
                CF[k[0]] += c[k]
            # CF[k[1]] += 1
            CF[S[-1]] += 1
            # diff = max(CF.values()) - min(CF.values())
            if i == 9:
                diff10 = max(CF.values()) - min(CF.values())
            elif i == 39:
                diff40 = max(CF.values()) - min(CF.values())
    return diff10, diff40


if __name__ == '__main__':
    # Parse input data
    X = [x.strip() for x in open(FILE_PATH, 'r')]
    XS, Y = [], []
    flag = False
    for x in X:
        if x == '':
            flag = True
            continue
        if not flag:
            XS.append(x)
        else:
            Y.append(x)

    S = XS[0]
    M = dict()
    for i in [y.split(' -> ') for y in Y]:
        M[i[0]] = i[1]
    D = deque([S[i:i+2] for i in range(len(S) - 1)])
    C = Counter(D)
    print(p1(M, C, iter=40))
