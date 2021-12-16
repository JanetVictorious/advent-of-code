import os
from collections import defaultdict, Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day7.csv'))

data = pd.read_csv(file_path, header=None, dtype='int')

start_arr = np.array(data.values[0])

X = Counter([int(x) for x in start_arr])


def _sum_int(x: int):
    val = float(x) * (float(x) + 1.0) / 2.0
    return int(val)


def solve(S, n, m):
    res = 1e6
    pos = np.nan
    X = S
    for move in range(n, m + 1):
        Y = defaultdict(int)
        for x, cnt in X.items():
            Y[x] = abs(x - move) * cnt

        if sum(Y.values()) < res:
            res = sum(Y.values())
            pos = move

    return res, pos


def solve2(S, n, m):
    res = 1e9
    pos = np.nan
    X = S
    for move in range(n, m + 1):
        Y = defaultdict(int)
        for x, cnt in X.items():
            Y[x] = _sum_int(abs(x - move)) * cnt

        if sum(Y.values()) < res:
            res = sum(Y.values())
            pos = move

    return res, pos


arr = np.copy(start_arr)
ones = np.ones(len(start_arr))

mu = np.mean(arr)
med = np.median(arr)

plt.figure(figsize=(12, 10))
sns.displot(arr, kind='kde')

lower_bound = int(med * 0.5)
upper_bound = int(med * 1.5)

# +--------------+
# |   Puzzle 1   |
# +--------------+

print(solve(X, lower_bound, upper_bound))

# +--------------+
# |   Puzzle 2   |
# +--------------+

print(solve2(X, lower_bound, upper_bound))
