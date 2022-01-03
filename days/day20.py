import os
from copy import deepcopy

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day20.in'))

data = open(file_path).read().strip()

rule, inpt_img = data.split('\n\n')

rule = rule.strip()
inpt_img = inpt_img.strip().split('\n')

assert len(rule) == 512

G = set()
for r, line in enumerate(inpt_img):
    for c, x in enumerate(line.strip()):
        if x == '#':
            G.add((r, c))


def show(S):
    x_min = min([x for x, y in S])
    x_max = max([x for x, y in S])
    y_min = min([y for x, y in S])
    y_max = max([y for x, y in S])
    for x in range(x_min - 5, x_max + 5):
        row = ''
        for y in range(y_min - 5, y_max + 5):
            if (x, y) in S:
                row += '#'
            else:
                row += '.'
        print(row)


def step(S, on):
    S2 = set()
    x_min = min([x for x, y in S])
    x_max = max([x for x, y in S])
    y_min = min([y for x, y in S])
    y_max = max([y for x, y in S])
    for x in range(x_min - 5, x_max + 10):
        for y in range(y_min - 5, y_max + 10):
            xy_pix = 0
            bit = 8
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if ((x + dx, y + dy) in S) == on:
                        xy_pix += 2**bit
                    bit -= 1
            assert 0 <= xy_pix < 512
            if (rule[xy_pix] == '#') != on:
                S2.add((x, y))
    return S2


# +------------------+
# |   Puzzle 1 + 2   |
# +------------------+

for t in range(50):
    # show(G)
    if t == 2:
        print(len(G))
    G = step(G, t % 2 == 0)
print(len(G))
