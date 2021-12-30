import os
from ast import literal_eval
import numpy as np

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day18.csv'))

inpt = np.genfromtxt(file_path, dtype=str)

arr = []
for line in inpt:
    assert line == line.strip()
    arr.append(literal_eval(line))


def explode(lst):
    s = str(lst).replace(' ', '')
    parts = []
    i = 0
    while i < len(s):
        if s[i] == '[':
            parts.append('[')
            i += 1
        elif s[i] == ',':
            parts.append(',')
            i += 1
        elif s[i] == ']':
            parts.append(']')
            i += 1
        elif s[i] == ' ':
            i += 1
        else:
            assert s[i].isdigit()
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            parts.append(int(s[i:j]))
            i = j

    dpth = 0
    for i, j in enumerate(parts):
        if j == '[':
            dpth += 1
            if dpth == 5:
                lft_v = parts[i + 1]
                assert isinstance(lft_v, int)
                assert parts[i + 2] == ','
                rght_v = parts[i + 3]
                assert isinstance(rght_v, int)
                lft_i = None
                rght_i = None
                for k in range(len(parts)):
                    if isinstance(parts[k], int) and k < i:
                        lft_i = k
                    elif isinstance(parts[k], int) and k > i + 3 and rght_i is None:
                        rght_i = k
                if rght_i is not None:
                    assert rght_i > i
                    parts[rght_i] += rght_v
                parts = parts[:i] + [0] + parts[i + 5:]
                if lft_i is not None:
                    parts[lft_i] += lft_v
                return True, literal_eval(''.join([str(x) for x in parts]))
        elif j == ']':
            dpth -= 1
        else:
            pass
    return False, lst


def split(lst):
    if isinstance(lst, list):
        flg1, lst1 = split(lst[0])
        if flg1:
            return True, [lst1, lst[1]]
        else:
            flg2, lst2 = split(lst[1])
            return flg2, [lst1, lst2]
    else:
        assert isinstance(lst, int)
        if lst >= 10:
            return True, [lst // 2, (lst + 1) // 2]
        else:
            return False, lst


def add_(l1, l2):
    lst = [l1, l2]
    return reduce_(lst)


def reduce_(lst):
    flg1, lst1 = explode(lst)
    if flg1:
        return reduce_(lst1)
    else:
        flg2, lst2 = split(lst)
        if flg2:
            return reduce_(lst2)
        else:
            return lst2


def magn(lst):
    if isinstance(lst, list):
        return 3 * magn(lst[0]) + 2 * magn(lst[1])
    else:
        return lst


# +------------------+
# |   Puzzle 1 + 2   |
# +------------------+

for i in range(len(arr) - 1):
    if i == 0:
        first = arr[i]
        second = arr[i + 1]
        next = add_(first, second)
    elif i == len(arr) - 2:
        score = magn(add_(next, arr[i + 1]))
    else:
        next = add_(next, arr[i + 1])

print(score)

mag = None
for x in arr:
    for y in arr:
        if x != y:
            score = magn(add_(x, y))
            if mag is None or score > mag:
                mag = score
print(mag)
