import os
from copy import deepcopy
from collections import deque, Counter

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '11.in'))


def p1(S, V, part=1):
    C = Counter(S.keys())
    for _ in range(20 if part == 1 else 10000):
        for k in S.keys():
            D = S[k]
            while D:
                d = D.popleft()
                C.update([k])
                op, val = V[k]['operation'].split(' ')

                if op == '+':
                    v = d + d if val == 'old' else d + int(val)
                elif op == '-':
                    v = d - d if val == 'old' else d - int(val)
                elif op == '*':
                    v = d * d if val == 'old' else d * int(val)

                v = v // 3 if part == 1 else v % DENOM

                if v % V[k]['test'] == 0:
                    S['Monkey ' + str(V[k]['true'])].append(v)
                else:
                    S['Monkey ' + str(V[k]['false'])].append(v)
    res = (C.most_common(2)[0][1] - 1) * (C.most_common(2)[1][1] - 1)
    return res


if __name__ == '__main__':
    X = [x for x in open(FILE_PATH, 'r')]
    M = dict()
    R = dict()
    DENOM = 1
    for x in X:
        if x.startswith('Monkey'):
            M[x[:8]] = deque()
            R[x[:8]] = dict()
            m = M[x[:8]]
            r = R[x[:8]]
        elif x.startswith('  Starting'):
            _, v = x.split(':')
            for vv in v.split(','):
                m.append(int(vv.strip()))
        elif x.startswith('  Operation'):
            _, v = x.split(':')
            v = v.replace('new = old', '').strip()
            r['operation'] = v
        elif x.startswith('  Test'):
            _, v = x.split(':')
            v = v.replace('divisible by', '').strip()
            r['test'] = int(v)
            DENOM *= int(v)
        elif x.startswith('    If true'):
            _, v = x.split(':')
            v = v.replace('throw to monkey', '').strip()
            r['true'] = int(v)
        elif x.startswith('    If false'):
            _, v = x.split(':')
            v = v.replace('throw to monkey', '').strip()
            r['false'] = int(v)
    M1 = deepcopy(M)
    M2 = deepcopy(M)
    print(p1(M1, R))
    print(p1(M2, R, part=2))
