import os
from collections import deque

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '09.in'))


def p1(S):
    risk_lvl = 0
    for x in range(len(S)):
        for y in range(len(S[0])):
            pnt = S[x][y]
            up = S[x-1][y] if x > 0 else 99
            dwn = S[x+1][y] if x < len(S) - 1 else 99
            lft = S[x][y-1] if y > 0 else 99
            rgh = S[x][y+1] if y < len(S[0]) - 1 else 99
            if pnt < up and pnt < dwn:
                if pnt < lft and pnt < rgh:
                    risk_lvl += pnt + 1

    return risk_lvl


DX = [-1, 0, 1, 0]
DY = [0, -1, 0, 1]


def p2(S):
    B = []
    Z = set()
    for x in range(len(S)):
        for y in range(len(S[0])):
            if (x, y) not in Z and S[x][y] != 9:
                size = 0
                Q = deque()
                Q.append((x, y))
                while Q:
                    (x, y) = Q.popleft()

                    if (x, y) in Z:
                        continue

                    Z.add((x, y))
                    size += 1

                    for i in range(4):
                        x2 = x + DX[i]
                        y2 = y + DY[i]
                        if 0 <= x2 < len(S) and 0 <= y2 < len(S[0]) and S[x2][y2] != 9:  # noqa: E501
                            Q.append((x2, y2))

                B += [size]
    prod = 1
    for p in sorted(B)[-3:]:
        prod *= p
    return prod


if __name__ == '__main__':
    # Parse input data
    X = [list(map(int, x.strip())) for x in open(FILE_PATH, 'r')]

    print(p1(X))
    print(p2(X))
