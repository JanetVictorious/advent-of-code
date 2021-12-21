import os
from collections import OrderedDict, defaultdict, Counter, deque
import numpy as np

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day14.csv'))

T = 'VOKKVSKKPSBVOOKVCFOV'
values = np.genfromtxt(file_path, dtype=str)

D = defaultdict(str)

val_arr = []
for v in values:
    D[v[0]] = v[2]

S = deque()
for i in range(len(T) - 1):
    S.append(str(T[i:i+2]))

X = Counter([str(s) for s in S])

for i in range(40):
    Y = Counter()
    for k in X:
        Y[k[0] + D[k]] += X[k]
        Y[D[k] + k[1]] += X[k]
    X = Y

    if i in [9, 39]:
        CF = Counter()
        for p in X:
            CF[p[0]] += X[p]

        CF[T[-1]] += 1
        print(f'Diff after {i + 1} steps: {max(CF.values()) - min(CF.values())}')
