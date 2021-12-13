import os
import numpy as np
import pandas as pd


base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day3.csv'))

data = pd.read_csv(file_path, header=None, dtype='str')

data.columns = ['bits']

data_split = data['bits'].str.split('', expand=True)
data_split = data_split.iloc[:, 1:-1].astype('int')

# +--------------+
# |   Puzzle 1   |
# +--------------+

gamma_rate = round(data_split.sum(axis=0) / data_split.shape[0]).astype('int')
epsilon_rate = gamma_rate.apply(lambda x: 0 if x == 1 else 1)

decimal_gamma = 0.0
for digit in gamma_rate:
    decimal_gamma = decimal_gamma * 2 + int(digit)

decimal_epsilon = 0.0
for digit in epsilon_rate:
    decimal_epsilon = decimal_epsilon * 2 + int(digit)

print(f'Gamma decimal = {decimal_gamma}')
print(f'Epsilon decimal = {decimal_epsilon}')
print(f'Product: {int(decimal_gamma * decimal_epsilon)}')


# +--------------+
# |   Puzzle 2   |
# +--------------+

data_oxygen = data_split
data_co2 = data_split

j = 1
for plc in range(1, data_oxygen.shape[1] + 1):
    val = data_oxygen[plc].value_counts().sort_index()
    val1 = val[0]
    idx1 = val.index[0]

    val2 = val[1]
    idx2 = val.index[1]

    if val1 > val2:
        idx = idx1
    elif val1 < val2:
        idx = idx2
    else:
        idx = idx2

    data_oxygen = data_oxygen.loc[
        data_oxygen[plc] == int(idx)
    ]

    if data_oxygen.shape[0] == 1:
        break

    j += 1

print(f'Final bit found at position {j}')

k = 1
for plc in range(1, data_co2.shape[1] + 1):
    val = data_co2[plc].value_counts().sort_index()
    val1 = val[0]
    idx1 = val.index[0]

    val2 = val[1]
    idx2 = val.index[1]

    if val1 > val2:
        idx = idx2
    elif val1 < val2:
        idx = idx1
    else:
        idx = idx1

    data_co2 = data_co2.loc[
        data_co2[plc] == int(idx)
    ]

    if data_co2.shape[0] == 1:
        break

    k += 1

print(f'Final bit found at position {k}')

decimal_oxygen = 0.0
for digit in data_oxygen.values[0]:
    decimal_oxygen = decimal_oxygen * 2 + int(digit)

decimal_co2 = 0.0
for digit in data_co2.values[0]:
    decimal_co2 = decimal_co2 * 2 + int(digit)

print(f'Oxygen decimal = {decimal_oxygen}')
print(f'CO2 decimal = {decimal_co2}')
print(f'Product: {int(decimal_oxygen * decimal_co2)}')
