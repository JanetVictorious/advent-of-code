import os
from collections import defaultdict, deque

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '12.in'))


def p1(D, part2=False):
    start = ('start', set(['start']), None)
    ans = 0
    Q = deque([start])
    while Q:
        pos, small, twice = Q.popleft()
        if pos == 'end':
            ans += 1
            continue
        for y in D[pos]:
            if y not in small:
                new_small = set(small)
                if y.islower():
                    new_small.add(y)
                Q.append((y, new_small, twice))
            elif y in small and twice is None and y not in ['start', 'end'] and part2:  # noqa: E501
                Q.append((y, small, y))
    return ans


if __name__ == '__main__':
    # Parse input data
    X = [x for x in open(FILE_PATH, 'r')]
    E = defaultdict(list)
    for line in X:
        a, b = line.strip().split('-')
        E[a].append(b)
        E[b].append(a)

    print(p1(E))
    print(p1(E, part2=True))
