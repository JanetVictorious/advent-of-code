import os
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day9.csv'))

values = np.genfromtxt(file_path, dtype=str)

mat = np.ndarray((values.shape[0], len(values[0])), order='C')

for idx, i in zip(range(mat.shape[0]), values):
    for cdx, j in zip(range(mat.shape[1]), i):
        mat[idx, cdx] = int(j)

# +--------------+
# |   Puzzle 1   |
# +--------------+

val = 0
D = {}

for idx in range(mat.shape[0]):
    for cdx in range(mat.shape[1]):
        v = mat[idx, cdx]

        try:
            u = mat[idx + 1, cdx]
        except IndexError:
            u = 1e6

        try:
            d = mat[idx - 1, cdx]
        except IndexError:
            d = 1e6

        try:
            l = mat[idx, cdx - 1]
        except IndexError:
            l = 1e6

        try:
            r = mat[idx, cdx + 1]
        except IndexError:
            r = 1e6

        if (v < u) & (v < d) & (v < l) & (v < r):
            val += v + 1
            D[str([idx, cdx])] = int(v)

print(f'Final sum = {int(val)}')
print(f'Nr of low points = {len(D.keys())}')

# +--------------+
# |   Puzzle 2   |
# +--------------+

plt.figure(figsize=(12, 10))
sns.heatmap(mat)

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

bas_size = []
S = set()

for idx in range(mat.shape[0]):
    for cdx in range(mat.shape[1]):
        if (idx, cdx) not in S and mat[idx, cdx] != 9:
            size = 0
            Q = deque()
            Q.append((idx, cdx))
            while Q:
                (idx, cdx) = Q.popleft()

                if (idx, cdx) in S:
                    continue

                S.add((idx, cdx))
                size += 1

                for d in range(4):
                    idx2 = idx + DR[d]
                    cdx2 = cdx + DC[d]
                    if 0 <= idx2 < mat.shape[0] and 0 <= cdx2 < mat.shape[1] and mat[idx2, cdx2] != 9:
                        Q.append((idx2, cdx2))

            bas_size += [size]

bas_size.sort()

print(bas_size[-1] * bas_size[-2] * bas_size[-3])
