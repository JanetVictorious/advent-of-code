import os
import pandas as pd


base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data/day2.csv')

data = pd.read_csv(file_path, header=None)

data.columns = ['command']

data['command']
com_list = data['command'].str.split()

com_list

# +--------------+
# |   Puzzle 1   |
# +--------------+

x = 0
y = 0
for i in com_list:
    if i[0] == 'forward':
        x += int(i[1])
    elif i[0] == 'down':
        y += int(i[1])
    else:
        y += -int(i[1])

print(f'Horisontal position: {x}')
print(f'Dept position: {y}')

print(f'x * y = {x * y}')


# +--------------+
# |   Puzzle 2   |
# +--------------+

x = 0
y = 0
aim = 0
for i in com_list:
    if i[0] == 'forward':
        x += int(i[1])
        if y > 0:
            aim += int(i[1]) * y
    elif i[0] == 'down':
        y += int(i[1])
    else:
        y += -int(i[1])

print(f'Horisontal position: {x}')
print(f'Dept position: {y}')
print(f'Aim position: {aim}')

print(f'x * aim = {x * aim}')
