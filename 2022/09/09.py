import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '09.in'))

DX = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
DY = {'L': 0, 'U': 1, 'R': 0, 'D': -1}


def movement(h, t):
    hx, hy = h
    tx, ty = t
    dx = (hx - tx)
    dy = (hy - ty)
    if abs(dx) <= 1 and abs(dy) <= 1:
        pass
    elif (abs(dx) >= 2 and abs(dy) >= 1) or (abs(dx) >= 1 and abs(dy) >= 2):
        t = (tx + 1 if hx > tx else tx - 1, ty + 1 if hy > ty else ty - 1)
    elif abs(dx) >= 2:
        t = (tx + 1 if hx > tx else tx - 1, hy)
    elif abs(dy) >= 2:
        t = (hx, ty + 1 if hy > ty else ty - 1)
    return t


def p1(S):
    T1 = set()
    T2 = set()
    TS = [(0, 0) for _ in range(9)]
    start = (0, 0)
    H = (0, 0)
    T1.add(start)
    T2.add(start)
    t = (0, 0)
    for s in S:
        d, m = s
        for _ in range(int(m)):
            H = (H[0] + DX[d], H[1] + DY[d])
            TS[0] = movement(H, TS[0])
            T1.add(TS[0])
            for i in range(1, 9):
                TS[i] = movement(TS[i-1], TS[i])
            T2.add(TS[-1])
    return len(T1), len(T2)


if __name__ == '__main__':
    X = [x.strip().split() for x in open(FILE_PATH, 'r')]
    print(p1(X))
