import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day5.csv'))

data = pd.read_csv(file_path, dtype='int')

# +--------------+
# |   Puzzle 1   |
# +--------------+

data2 = data.loc[
    (data['x1'] == data['x2']) | (data['y1'] == data['y2'])
].reset_index(drop=True)

data2['type'] = np.where(data2['x1'] == data2['x2'],
                         'vertical',
                         'horisontal')

plt.figure(figsize=(10, 12))
for i in data2.index:
    x = [data2.iloc[i, 0], data2.iloc[i, 2]]
    y = [data2.iloc[i, 1], data2.iloc[i, 3]]
    plt.plot(x, y, color='b')

x_min = np.min([data2['x1'].min(), data2['x2'].min()])
x_max = np.max([data2['x1'].max(), data2['x2'].max()])

y_min = np.min([data2['y1'].min(), data2['y2'].min()])
y_max = np.max([data2['y1'].max(), data2['y2'].max()])

grid = np.ndarray(shape=(x_max + 1, y_max + 1), order='C')
grid[:, :] = 0.0

for x1, y1, x2, y2 in zip(data2['x1'], data2['y1'], data2['x2'], data2['y2']):
    x_min = np.min([x1, x2])
    x_max = np.max([x1, x2])
    y_min = np.min([y1, y2])
    y_max = np.max([y1, y2])

    if x_min == x_max:
        grid[x_min, (y_min):(y_max + 1)] += 1.0
    elif y_min == y_max:
        grid[(x_min):(x_max + 1), y_min] += 1.0

nr_cross = len(grid[np.where(grid >= 2)])

print(f'Nr of intersecting points = {nr_cross}')

# +--------------+
# |   Puzzle 2   |
# +--------------+

plt.figure(figsize=(10, 12))
for i in data.index:
    x = [data.iloc[i, 0], data.iloc[i, 2]]
    y = [data.iloc[i, 1], data.iloc[i, 3]]
    plt.plot(x, y, color='b')

x_min = np.min([data['x1'].min(), data['x2'].min()])
x_max = np.max([data['x1'].max(), data['x2'].max()])

y_min = np.min([data['y1'].min(), data['y2'].min()])
y_max = np.max([data['y1'].max(), data['y2'].max()])

grid_diag = np.ndarray(shape=(x_max + 1, y_max + 1), order='C')
grid_diag[:, :] = 0.0

for x1, y1, x2, y2 in zip(data['x1'], data['y1'], data['x2'], data['y2']):
    x_min = np.min([x1, x2])
    x_max = np.max([x1, x2])
    y_min = np.min([y1, y2])
    y_max = np.max([y1, y2])

    if x_min == x_max:
        grid_diag[x_min, (y_min):(y_max + 1)] += 1.0
    elif y_min == y_max:
        grid_diag[(x_min):(x_max + 1), y_min] += 1.0
    else:
        if x1 < x2:
            if y1 < y2:
                for i in range(x1, x2 + 1):
                    j = i - x1
                    grid_diag[i, y1 + j] += 1
            else:
                for i in range(x1, x2 + 1):
                    j = i - x1
                    grid_diag[i, y1 - j] += 1
        else:
            if y1 < y2:
                for i in range(x2, x1 + 1):
                    j = i - x2
                    grid_diag[i, y2 - j] += 1
            else:
                for i in range(x2, x1 + 1):
                    j = i - x2
                    grid_diag[i, y2 + j] += 1

nr_cross_diag = len(grid_diag[np.where(grid_diag >= 2)])

print(f'Nr of intersecting points = {nr_cross_diag}')
