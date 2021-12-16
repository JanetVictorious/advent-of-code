import os
import numpy as np

base_path = os.path.dirname(__file__)
file_path_1 = os.path.abspath(
    os.path.join(base_path, '..', 'data/day8_signals.csv'))
file_path_2 = os.path.abspath(
    os.path.join(base_path, '..', 'data/day8_outputs.csv'))

signals = np.genfromtxt(file_path_1, dtype=str)
outputs = np.genfromtxt(file_path_2, dtype=str)

digit_dict = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

# +--------------+
# |   Puzzle 1   |
# +--------------+

output_len = np.vectorize(len)

output_2 = output_len(outputs)

nr_val = np.isin(output_2, [2, 3, 4, 7]).sum()

print(f'Nr of 1, 4, 7, 8: {nr_val}')


# +--------------+
# |   Puzzle 2   |
# +--------------+

def get_output_val(input_arr, output_arr):
    D = {}

    for s in input_arr:
        if len(s) == 2:  # 1
            cf = s

    for s in input_arr:
        if len(s) == 3:  # 7
            for i in s:
                if i not in cf:
                    a = i
                    D[str(i)] = 'a'

    for s in input_arr:
        if (len(s) == 6) & ((cf[0] in s) != (cf[1] in s)):  # 6
            if cf[0] in s:
                c = cf[1]
                f = cf[0]
                D[cf[0]] = 'f'
                D[cf[1]] = 'c'
            else:
                c = cf[0]
                f = cf[1]
                D[cf[0]] = 'c'
                D[cf[1]] = 'f'

    for s in input_arr:
        if (len(s) == 5) & (cf[0] in s) & (cf[1] in s):  # 3
            dg = ''
            for i in s:
                if (i in cf) | (i in a):
                    pass
                else:
                    dg += i

    for s in input_arr:
        if (len(s) == 6) & (a in s) & (cf[0] in s) & (cf[1] in s) & (dg[0] in s) & (dg[1] in s):  # 9
            for i in s:
                if (i in a) | (i in cf) | (i in dg):
                    pass
                else:
                    b = i
                    D[str(i)] = 'b'

    for s in input_arr:
        if (len(s) == 4):  # 4
            for i in s:
                if (i in cf) | (i in b):
                    pass
                else:
                    d = i
                    D[str(i)] = 'd'
                    if d == dg[0]:
                        g = dg[1]
                        D[dg[1]] = 'g'
                    else:
                        g = dg[0]
                        D[dg[0]] = 'g'

    for s in input_arr:
        if (len(s) == 6) & (c not in s):  # 6
            for i in s:
                if (i in a) | (i in b) | (i in d) | (i in f) | (i in g):
                    pass
                else:
                    e = i
                    D[str(i)] = 'e'

    D = dict(sorted(D.items()))

    X = []

    for s in output_arr:
        o = list(s)
        for i in range(len(s)):
            o[i] = D[s[i]]

        o2 = ''.join(sorted(o))
        X += [o2]

    val = []

    for v in X:
        for n, k in digit_dict.items():
            if v == k:
                val += [str(n)]

    return int(''.join(val))


num_arr = []

for inp, out in zip(signals, outputs):
    num_arr += [get_output_val(inp, out)]

print(f'Final sum: {sum(num_arr)}')
