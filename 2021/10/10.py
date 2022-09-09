import os
from collections import deque

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '10.in'))


def p1(S):
    prod = 0
    for s in S:
        Q = deque()
        val = 0
        for x in s:
            Q.append(x)

            if x in ['(', '[', '{', '<']:
                continue

            n, p = Q.pop(), Q.pop()

            if n in [')', ']', '}', '>']:
                if p + n not in ['()', '[]', '{}', '<>']:
                    if n == ')':
                        val += 3
                    if n == ']':
                        val += 57
                    if n == '}':
                        val += 1197
                    if n == '>':
                        val += 25137
                    break
                else:
                    continue
        prod += val
    return prod


def p2(S):
    P = []
    for s in S:
        broken = False
        Q = deque()
        val = 0

        for x in s:
            Q.append(x)

            if x in ['(', '[', '{', '<']:
                continue

            n, p = Q.pop(), Q.pop()

            if n in [')', ']', '}', '>']:
                if p + n not in ['()', '[]', '{}', '<>']:
                    broken = True
                    break
                else:
                    continue

        while Q and not broken:
            q = Q.pop()
            val *= 5
            if q == '(':
                val += 1
            elif q == '[':
                val += 2
            elif q == '{':
                val += 3
            else:
                val += 4

        if not broken:
            P += [val]

    P = sorted(P)
    mid_idx = int((len(P) - 1) / 2)
    return P[mid_idx]


if __name__ == '__main__':
    # Parse input data
    X = [x.strip() for x in open(FILE_PATH, 'r')]

    print(p1(X))
    print(p2(X))
