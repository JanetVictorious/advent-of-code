import os
import numpy as np
import pandas as pd


base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data/day3.csv')

data = pd.read_csv(file_path, header=None, dtype='str')

data.columns = ['bits']

# +--------------+
# |   Puzzle 1   |
# +--------------+

data_split = data['bits'].str.split('', expand=True)
data_split = data_split.iloc[:, 1:-1].astype('int')

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
