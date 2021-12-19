import os
from collections import Counter, deque
import numpy as np

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day11.csv'))

values = np.genfromtxt(file_path, dtype=str)

mat = np.ndarray((values.shape[0], len(values[0])), order='C')

for idx, i in zip(range(mat.shape[0]), values):
    for cdx, j in zip(range(mat.shape[1]), i):
        mat[idx, cdx] = int(j)

# +------------------+
# |   Puzzle 1 + 2   |
# +------------------+

DR = [-1, 0, 1]
DC = [-1, 0, 1]

r = mat.shape[0]
c = mat.shape[1]

F = 0


def flash(idx, cdx):
    global F
    F += 1
    mat[idx, cdx] = -1
    for i in DR:
        for j in DC:
            idx2 = idx + i
            cdx2 = cdx + j
            if 0 <= idx2 < r and 0 <= cdx2 < c and mat[idx2, cdx2] != -1:
                mat[idx2, cdx2] += 1
                if mat[idx2, cdx2] >= 10:
                    flash(idx2, cdx2)


it = 0
while True:
    it += 1

    for idx in range(r):
        for cdx in range(c):
            mat[idx, cdx] += 1

    for idx in range(r):
        for cdx in range(c):
            if mat[idx, cdx] == 10:
                flash(idx, cdx)

    ok = True
    for idx in range(r):
        for cdx in range(c):
            if mat[idx, cdx] == -1:
                mat[idx, cdx] = 0
            else:
                ok = False

    if it == 100:
        print(F)

    if ok:
        print(it)
        break


# for it in range(10):
#     S = set()
#     for idx in range(r):
#         for cdx in range(c):
#             if (idx, cdx) not in S:  # and mat[idx, cdx] != 0:
#                 # flash = 0
#                 Q = deque()
#                 Q.append((idx, cdx))
#                 while Q:
#                     (idx, cdx) = Q.popleft()

#                     if (idx, cdx) in S:
#                         continue

#                     mat[idx, cdx] += 1

#                     if mat[idx, cdx] > 9:
#                         F += 1
#                         mat[idx, cdx] = 0
#                         S.add((idx, cdx))

#                         for i in range(len(DR)):
#                             idx2 = idx + DR[i]
#                             cdx2 = cdx + DC[i]
#                             if 0 <= idx2 < r and 0 <= cdx2 < c:  # and mat[idx2, cdx2] != 0:
#                                 Q.append((idx2, cdx2))
#                                 mat[idx2, cdx2] += 1
#                 # F += flash
#     print('-' * 50)
#     print(f'Iteration: {it + 1}')
#     print(mat)

# print(f'Nr of flashes after {it + 1} steps = {int(F)}')
