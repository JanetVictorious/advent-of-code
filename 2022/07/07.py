import os
from collections import deque

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '07.in'))


def p1(S):
    C = dict()
    T = dict()
    prev_dir = deque()
    for s in S:
        if s[0] == '$':
            if s[1] == 'cd':
                dirname = s[2]
                if dirname == '/':
                    T[dirname] = dict()
                    d = T[dirname]
                    C[dirname] = 0
                elif dirname == '..':
                    prev_dir.pop()
                    d = T['/']
                    for i in prev_dir:
                        d = d[i]
                else:
                    d = d[dirname]
                    prev_dir.append(dirname)
            elif s[1] == 'ls':
                continue
        else:
            if s[0] == 'dir':
                d[s[1]] = dict()
                d_n = '/' + '/'.join(list(prev_dir) + [s[1]])
                C[d_n] = 0
            else:
                d[s[1]] = int(s[0])
                m = len(prev_dir) + 1
                for i in range(m):
                    ss = '/' + '/'.join(list(prev_dir)[0:i])
                    C[ss] += int(s[0])

    val = 0
    for v in C.values():
        if v <= 100000:
            val += v

    diff = 70000000 - C.get('/')
    to_remove = 30000000 - diff
    C_sorted = dict(sorted(C.items(), key=lambda x: x[1]))
    for k, v in C_sorted.items():
        if v >= to_remove:
            break

    return val, {k: v}


if __name__ == '__main__':
    X = [x for x in open(FILE_PATH, 'r')]
    X = [x.split() for x in X]
    print(p1(X))
