import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '11.in'))

DX = [-1, 0, 1]
DY = [-1, 0, 1]
F = 0


def _flash(x, y, S):
    global F
    F += 1
    S[x][y] = -1
    for i in DX:
        for j in DY:
            x2 = x + i
            y2 = y + j
            if 0 <= x2 < len(S) and 0 <= y2 < len(S[0]) and S[x2][y2] != -1:
                S[x2][y2] += 1
                if S[x2][y2] >= 10:
                    _flash(x2, y2, S)


def p1(S):
    it = 0
    while True:
        it += 1

        for x in range(len(S)):
            for y in range(len(S[0])):
                S[x][y] += 1

        for x in range(len(S)):
            for y in range(len(S[0])):
                if S[x][y] == 10:
                    _flash(x, y, S)

        cont = True
        for x in range(len(S)):
            for y in range(len(S[0])):
                if S[x][y] == -1:
                    S[x][y] = 0
                else:
                    cont = False

        if it == 100:
            print(F)

        if cont:
            return it


if __name__ == '__main__':
    # Parse input data
    X = [list(map(int, x.strip())) for x in open(FILE_PATH, 'r')]

    print(p1(X))
