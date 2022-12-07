import os
from collections import deque, Counter

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '06.in'))


def p1(S, num=4):
    D = deque()
    for i in range(len(S)):
        s = S[i]
        if len(D) == num:
            break
        if s not in D:
            D.append(s)
            if any(x > 1 for x in Counter(D).values()):
                D.popleft()
            continue
        D.append(s)
        D.popleft()
    return S[i-num:i], i


if __name__ == '__main__':
    X = [x for x in open(FILE_PATH).read()]
    print(p1(X))
    print(p1(X, num=14))
