import os
from collections import deque
from copy import deepcopy

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '05.in'))


def p1(S, L):
    for m in L:
        for _ in range(m[0]):
            v = S[m[1]].pop()
            S[m[2]].append(v)
    c = ''
    for k in S.keys():
        v = S[k].pop()
        c += v
    return c


def p2(S, L):
    for m in L:
        cs = []
        for _ in range(m[0]):
            v = S[m[1]].pop()
            cs.append(v)
        for c in reversed(cs):
            S[m[2]].append(c)
    c = ''
    for k in S.keys():
        v = S[k].pop()
        c += v
    return c


if __name__ == '__main__':
    X = [x.replace('\n', '') for x in open(FILE_PATH, 'r')]
    D = {}
    c_n = len(X[0]) // 4 + 1
    for c in range(1, c_n+1):
        D[c] = deque()
    C = []
    M = []
    flag = False
    for x in X:
        if x == '':
            flag = True
            continue
        if flag:
            y = x.replace('move', '').replace('from', '').replace('to', '').split()
            M.append([int(y) for y in y])
        else:
            C.append(x)
    C = C[:-1]
    for i in reversed(range(len(C))):
        x = C[i]
        for j in range(c_n):
            y = x[j*4:(j+1)*4]
            if y.strip() == '':
                continue
            y = y.strip().replace('[', '').replace(']', '')
            D[j+1].append(y)
    D1 = deepcopy(D)
    D2 = deepcopy(D)
    print(p1(D1, M))
    print(p2(D2, M))
