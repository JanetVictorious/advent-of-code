import os
from collections import Counter

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '06.in'))


def p1(D, cnt=80):
    for _ in range(cnt):
        rebooted_fish = 0
        born_fish = 0
        for d in range(9):
            nr_fish = D.get(d)

            if not nr_fish:
                continue

            if d == 0:
                D[0] = 0
                rebooted_fish = nr_fish
                born_fish = nr_fish
            else:
                D[d] -= nr_fish
                D[d-1] += nr_fish
        D[6] += rebooted_fish
        D[8] += born_fish

    return sum(D.values())


if __name__ == '__main__':
    # Parse input data
    S = open(FILE_PATH, 'r').read()
    s = Counter([int(x) for x in S.split(',')])
    d = {}
    for i in range(9):
        d[i] = 0
    X = Counter(d)
    X.update(s)

    print(p1(X, cnt=80))

    # Reset counter
    X = Counter(d)
    X.update(s)

    print(p1(X, cnt=256))
