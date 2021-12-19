import os
import numpy as np

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day10.csv'))

chunks = np.genfromtxt(file_path, dtype=str)

chunks.shape
chunks[0]
len(chunks[0])

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score2 = {
    ')': 1.0,
    ']': 2.0,
    '}': 3.0,
    '>': 4.0
}

# +-----------------+
# |   Puzzle 1 + 2  |
# +-----------------+

error_score = 0
completion_score = []

for c in chunks:
    v = []
    ok = True
    for i in c:
        if i == '(':
            v.append(')')
        elif i == '[':
            v.append(']')
        elif i == '{':
            v.append('}')
        elif i == '<':
            v.append('>')
        else:
            if v[-1] == i:
                v = v[:-1]
            else:
                error_score += score.get(i, 0)
                ok = False
                break
    else:
        if ok:
            comp_score = 0.0
            for t in v[::-1]:
                comp_score = (comp_score * 5.0 + score2.get(t, 0.0))
            completion_score.append(comp_score)

print(f'Error score = {int(error_score)}')
print(f'Median completion score = {int(np.median(completion_score))}')
