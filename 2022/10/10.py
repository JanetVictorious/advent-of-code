import os
from collections import deque
import numpy as np

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '10.in'))


def p1(S):
    x = 1
    cycle = 1
    signal = 0
    D = deque(S)
    crt = np.array([['.'] * 40]*6).reshape(6, 40)
    row = 0
    while D:
        d = D.popleft()
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal += cycle * x
        sprite = [x-1, x, x+1]
        pxl_pos = 39 if cycle % 40 == 0 else cycle % 40 - 1
        if pxl_pos in sprite:
            crt[row, pxl_pos] = '#'
        if cycle % 40 == 0:
            row += 1
        if d[0] == 'noop':
            pass
        elif d[0] == 'addx':
            val = int(d[1])
            D = deque([['exec', val]]) + D
        elif d[0] == 'exec':
            x += d[1]
        cycle += 1
    for r in crt:
        print(''.join(r))
    return signal


if __name__ == '__main__':
    X = [x.strip().split() for x in open(FILE_PATH, 'r')]
    print(p1(X))
