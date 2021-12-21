import heapq
import os
import numpy as np

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day15.csv'))

values = np.genfromtxt(file_path, dtype=str)

# values = np.array(['1163751742',
#                    '1381373672',
#                    '2136511328',
#                    '3694931569',
#                    '7463417111',
#                    '1319128137',
#                    '1359912421',
#                    '3125421639',
#                    '1293138521',
#                    '2311944581'])

mat = np.ndarray((values.shape[0], len(values[0])), order='C')

for idx, i in zip(range(mat.shape[0]), values):
    for cdx, j in zip(range(mat.shape[1]), i):
        mat[idx, cdx] = int(j)

R = mat.shape[0]
C = mat.shape[1]
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]


def solve(n):
    start = (0, 0, 0)
    end = (n * R - 1, n * C - 1)

    D = np.array([[None for _ in range(n * C)] for _ in range(n * R)])
    Q = [(start)]

    while Q:
        dist, x, y = heapq.heappop(Q)

        if x < 0 or x >= n * R or y < 0 or y >= n * C:
            continue

        val = mat[x % R, y % C] + (x // R) + (y // C)

        while val > 9:
            val -= 9

        xy_cost = dist + val

        if D[x, y] is None or xy_cost < D[x, y]:
            D[x, y] = xy_cost
        else:
            continue

        if (x, y) == end:
            break

        for i in range(4):
            x2 = x + DR[i]
            y2 = y + DC[i]
            heapq.heappush(Q, (D[x, y], x2, y2))

    return D[n * R - 1, n * C - 1] - mat[0, 0]


# +------------------+
# |   Puzzle 1 + 2   |
# +------------------+

print(solve(1))
print(solve(5))
