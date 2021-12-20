from collections import Counter, defaultdict, deque
import os
import numpy as np

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day12.csv'))

values = np.genfromtxt(file_path, dtype=str)

E = defaultdict(list)
for line in values:
    a, b = line.strip().split('-')
    E[a].append(b)
    E[b].append(a)

# S = deque()


def solve(t):
    start = ('start', set(['start']), None)
    ans = 0
    Q = deque([start])
    while Q:
        pos, small, twice = Q.popleft()
        if pos == 'end':
            ans += 1
            continue
        for y in E[pos]:
            if y not in small:
                new_small = set(small)
                if y.islower():
                    new_small.add(y)
                Q.append((y, new_small, twice))
            elif y in small and twice is None and y not in ['start', 'end'] and not t:
                Q.append((y, small, y))

    return ans


print(solve(True))
print(solve(False))
