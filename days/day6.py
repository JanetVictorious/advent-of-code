import os
from collections import defaultdict, Counter
import numpy as np
import pandas as pd
from pyinstrument import Profiler

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day6.csv'))

data = pd.read_csv(file_path, header=None, dtype='int')

start_arr = np.array(data.values[0])

short_arr, counts = np.unique(start_arr, return_counts=True)

X = Counter([int(x) for x in start_arr])


def dev_arr(arr: np.array) -> np.array:
    old_arr = np.copy(arr)
    ones = np.ones(len(old_arr))

    arr[(old_arr - ones >= 0)] += -1
    arr[(old_arr - ones < 0)] = 6

    new_fish = [8] * (old_arr - ones < 0).sum()

    if new_fish:
        arr = np.concatenate((arr, new_fish))

    return arr


def solve(S, n):
    X = S
    for day in range(n):
        Y = defaultdict(int)
        for x, cnt in X.items():
            if x == 0:
                Y[6] += cnt
                Y[8] += cnt
            else:
                Y[x - 1] += cnt
        X = Y
    return sum(X.values())


# +--------------+
# |   Puzzle 1   |
# +--------------+

short_arr0 = np.array([short_arr[0]])
short_arr1 = np.array([short_arr[1]])
short_arr2 = np.array([short_arr[2]])
short_arr3 = np.array([short_arr[3]])
short_arr4 = np.array([short_arr[4]])

p1 = Profiler()
p1.start()

for i in range(80):
    short_arr0 = dev_arr(short_arr0)
    short_arr1 = dev_arr(short_arr1)
    short_arr2 = dev_arr(short_arr2)
    short_arr3 = dev_arr(short_arr3)
    short_arr4 = dev_arr(short_arr4)

tot_nr = (len(short_arr0) * counts[0] +
          len(short_arr1) * counts[1] +
          len(short_arr2) * counts[2] +
          len(short_arr3) * counts[3] +
          len(short_arr4) * counts[4])

print(f'Nr fish after {i + 1} days is {tot_nr}')

p1.stop()
p1.print()

# html1 = p1.output_html()
# display(HTML(html1))

print(solve(X, 80))

# +--------------+
# |   Puzzle 2   |
# +--------------+

print(solve(X, 256))
