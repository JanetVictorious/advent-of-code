import os
from collections import deque

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '13.in'))


def p1(X, Y):
    xmax = max([int(x.split(',')[0]) for x in X])
    ymax = max([int(x.split(',')[1]) for x in X])

    # Extract folds
    F = deque([y.strip('fold along ').split('=') for y in Y])

    xmax = max([xmax] + [int(i[1]) * 2 for i in F if i[0] == 'x'])
    ymax = max([ymax] + [int(i[1]) * 2 for i in F if i[0] == 'y'])

    # Create grid
    R = [list('.' * (xmax + 1)) for _ in range(ymax + 1)]
    for xy in X:
        x, y = tuple(map(int, xy.split(',')))
        R[y][x] = '#'

    # Fold
    cnt = 0
    R_adj = [[j for j in i] for i in R]
    while F:
        # ax, n = F[i][0], int(F[i][1])
        ax, n = F.popleft()
        n = int(n)

        if ax == 'y':
            r1 = [[j for j in i] for i in R_adj[:n]]
            r2 = [R_adj[n+1:][r] for r in range(len(R_adj[n+1:])-1, -1, -1)]
        else:
            r1 = [[j for j in i][:n] for i in R_adj[:]]
            r2 = [list(reversed([j for j in i][n+1:])) for i in R_adj[:]]
        for r in range(len(r1)):
            for c in range(len(r1[0])):
                if r1[r][c] == '#' or r2[r][c] == '#':
                    r1[r][c] = '#'
        R_adj = [[j for j in i] for i in r1]
        if cnt == 0:
            for i in R_adj:
                for j in i:
                    if j == '#':
                        cnt += 1
    for i in R_adj:
        print(i)
    return cnt


if __name__ == '__main__':
    # Parse input data
    X = [x.strip() for x in open(FILE_PATH, 'r')]
    XS, IN = [], []
    flag = False
    for x in X:
        if x == '':
            flag = True
            continue
        if not flag:
            XS.append(x)
        else:
            IN.append(x)

    print(p1(XS, IN))
