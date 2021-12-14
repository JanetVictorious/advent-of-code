import os
import numpy as np
import pandas as pd


base_path = os.path.dirname(__file__)
file_path_1 = os.path.abspath(
    os.path.join(base_path, '..', 'data/day4_rnd_order.csv'))
file_path_2 = os.path.abspath(
    os.path.join(base_path, '..', 'data/day4_boards.csv'))

rnd_order = pd.read_csv(file_path_1, header=None, dtype='int')
boards = pd.read_csv(file_path_2, header=None, dtype='int')

rnd_order = np.array(rnd_order.values[0])

boards['board'] = np.nan

nr = 1
for i in boards.index:
    boards.iloc[i, 5] = int(nr)
    if i % 5 < 4:
        continue
    else:
        nr += 1

boards['board'] = boards['board'].astype('int')

# +--------------+
# |   Puzzle 1   |
# +--------------+

game = boards

for draw in rnd_order:
    cond = (game != draw)
    game = game[cond]
    game['board'] = boards['board']

    for brd in game['board'].unique():
        if any(i == 5
               for i in (game.loc[game['board'] == brd].isna().sum(axis=0))):
            print('BINGO!')
            score = game.loc[game['board'] == brd]\
                .drop(columns=['board']).sum().sum() * draw
            print(f"The final score is = {score}")
            break
        elif any(i == 5
                 for i in (game.loc[game['board'] == brd].isna().sum(axis=1))):
            print('BINGO!')
            score = game.loc[game['board'] == brd]\
                .drop(columns=['board']).sum().sum() * draw
            print(f"The final score is = {score}")
            break
    else:
        continue
    break

# +--------------+
# |   Puzzle 2   |
# +--------------+

game2 = boards
brds = game2['board'].unique()

for draw in rnd_order:
    cond = (game2 != draw)
    game2 = game2[cond]
    game2['board'] = boards['board']

    for brd in brds:
        if any(i == 5
               for i in (game2.loc[game2['board'] == brd].isna().sum(axis=0))):
            if len(brds) == 1:
                print('BINGO!')
                score = game2.loc[game2['board'] == brd]\
                    .drop(columns=['board']).sum().sum() * draw
                print(f"The final score is = {score}")
                print(f'For board {brd}')
                break
            brds = np.delete(brds, np.where(brds == brd))
        elif any(i == 5
                 for i in (game2.loc[game2['board'] == brd].isna().sum(axis=1))):
            if len(brds) == 1:
                print('BINGO!')
                score = game2.loc[game2['board'] == brd]\
                    .drop(columns=['board']).sum().sum() * draw
                print(f"The final score is = {score}")
                print(f'For board {brd}')
            brds = np.delete(brds, np.where(brds == brd))
    else:
        continue
    break
