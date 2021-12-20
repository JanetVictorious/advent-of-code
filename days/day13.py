import os
import numpy as np

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day13.csv'))
fold_path = os.path.abspath(os.path.join(base_path, '..', 'data/day13_fold.csv'))

values = np.genfromtxt(file_path, dtype=str)
folds = np.genfromtxt(fold_path, dtype=str)

fold_lst = []
for fld in folds[:, 2]:
    ax, idx = fld.strip().split('=')
    fold_lst += [(ax, int(idx))]

# values = np.array(['6,10',
#                    '0,14',
#                    '9,10',
#                    '0,3',
#                    '10,4',
#                    '4,11',
#                    '6,0',
#                    '6,12',
#                    '4,1',
#                    '0,13',
#                    '10,12',
#                    '3,4',
#                    '3,0',
#                    '8,4',
#                    '1,10',
#                    '2,14',
#                    '8,10',
#                    '9,0'])

# fold_lst = [('y', 7), ('x', 5)]

x_arr = []
y_arr = []
for s in values:
    x, y = s.strip().split(',')
    x_arr += [int(x)]
    y_arr += [int(y)]

fold_lst
x_max = 0
y_max = 0
for fld in fold_lst:
    ax, val = fld[0], fld[1]
    if ax == 'x':
        x_max = np.max([val * 2, x_max])
    if ax == 'y':
        y_max = np.max([val * 2, y_max])

mat = np.full((y_max + 1, x_max + 1), np.nan)

for y, x in zip(y_arr, x_arr):
    mat[y, x] = 1


def fold_y(mat, y_idx):
    mat_up = mat[:y_idx, :]
    mat_lw = mat[(y_idx + 1):, :]
    mat_lw_f = np.flip(mat_lw, 0)

    assert mat_up.shape == mat_lw_f.shape

    mat_mrg = mat_up
    for idx in range(mat_mrg.shape[0]):
        for cdx in range(mat_mrg.shape[1]):
            mat_mrg[idx, cdx] = np.where(np.isnan(mat_mrg[idx, cdx]),
                                         mat_lw_f[idx, cdx],
                                         mat_mrg[idx, cdx])

    return mat_mrg


def fold_x(mat, x_idx):
    mat_l = mat[:, :x_idx]
    mat_r = mat[:, (x_idx + 1):]
    mat_r_f = np.flip(mat_r, 1)

    assert mat_l.shape == mat_r_f.shape

    mat_mrg = mat_l
    for idx in range(mat_mrg.shape[0]):
        for cdx in range(mat_mrg.shape[1]):
            mat_mrg[idx, cdx] = np.where(np.isnan(mat_mrg[idx, cdx]),
                                         mat_r_f[idx, cdx],
                                         mat_mrg[idx, cdx])

    return mat_mrg


# mat_f1 = fold_y(mat, 7)
# np.nansum(mat_f1)

# mat_f2 = fold_x(mat_f1, 5)
# np.nansum(mat_f2)

mat_new = np.copy(mat)

t = 0
for fld in fold_lst:
    t += 1
    ax = fld[0]
    idx = fld[1]

    if ax == 'y':
        mat_mrg = fold_y(mat_new, idx)
    else:
        mat_mrg = fold_x(mat_new, idx)

    mat_new = np.copy(mat_mrg)

    if t == 1:
        print(int(np.nansum(mat_new)))

print(f'Nr of folds: {t}')
print(np.where(np.isnan(mat_new), '.', '#'))
