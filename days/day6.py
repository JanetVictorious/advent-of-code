import os
import numpy as np
import pandas as pd
from pyinstrument import Profiler
from IPython.core.display import display, HTML


base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day6.csv'))

data = pd.read_csv(file_path, header=None, dtype='int')

start_arr = np.array(data.values[0])

# +--------------+
# |   Puzzle 1   |
# +--------------+

p1 = Profiler()
p1.start()

arr = np.copy(start_arr)

for i in range(80):
    old_arr = np.copy(arr)
    ones = np.ones(len(old_arr))

    arr[(old_arr - ones >= 0)] += -1
    arr[(old_arr - ones < 0)] = 6

    new_fish = [8] * (old_arr - ones < 0).sum()

    if new_fish:
        arr = np.concatenate((arr, new_fish))

print(f'Nr fish after {i + 1} days is {len(arr)}')

p1.stop()
p1.print()

# html1 = p1.output_html()
# display(HTML(html1))

# +--------------+
# |   Puzzle 2   |
# +--------------+

p2 = Profiler()
p2.start()

arr = np.copy(start_arr)

for i in range(256):
    old_arr = np.copy(arr)
    ones = np.ones(len(old_arr))

    arr[(old_arr - ones >= 0)] += -1
    arr[(old_arr - ones < 0)] = 6

    new_fish = [8] * (old_arr - ones < 0).sum()

    if new_fish:
        arr = np.concatenate((arr, new_fish))

print(f'Nr fish after {i + 1} days is {len(arr)}')

p2.stop()
p2.print()

# html2 = p2.output_html()
# display(HTML(html2))
