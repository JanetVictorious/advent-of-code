import os
import numpy as np
import pandas as pd


base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data/day1.csv')

data = pd.read_csv(file_path, header=None)

meas = np.array(data.values)

# +--------------+
# |   Puzzle 1   |
# +--------------+

inc = 0
for previous, current in zip(meas, meas[1:]):
    if previous < current:
        print("increasing")
        inc += 1
    elif previous > current:
        print("decreasing")

print(f'Nr increases: {inc}')

# +--------------+
# |   Puzzle 2   |
# +--------------+

inc2 = 0
window_size = 3

for i in range(0, len(meas) - window_size + 1):
    if i == 0:
        inc2 = 0
    else:
        j = i - 1
        prev_window = sum(meas[j:(j + window_size)])
        curr_window = sum(meas[i:(i + window_size)])
        if prev_window < curr_window:
            inc2 += 1

print(f'Nr moving increases: {inc2}')
