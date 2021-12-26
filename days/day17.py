import os
import numpy as np

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day17.csv'))

trg_input = np.genfromtxt(file_path, dtype=str)

trg_area = {}
for s in trg_input:
    s = s.strip().replace(',', '')
    if s[0] in ['x', 'y']:
        ax = s[0]
        s = s.replace(s[0] + '=', '')
        v_min, v_max = s.split('..')
        trg_area[ax] = (int(v_min), int(v_max))

x_min = trg_area['x'][0]
x_max = trg_area['x'][1]
y_min = trg_area['y'][0]
y_max = trg_area['y'][1]

# +------------------+
# |   Puzzle 1 + 2   |
# +------------------+

p2 = 0
ans = 0
for DX in range(350):
    for DY in range(-100, 1000):
        ok = False
        max_y = 0
        x = 0
        y = 0
        dx = DX
        dy = DY
        for t in range(1000):
            x += dx
            y += dy
            max_y = max(max_y, y)
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1
            if x_min <= x <= x_max and y_min <= y <= y_max:
                ok = True
        if ok:
            p2 += 1
            if max_y > ans:
                ans = max_y
                print(DX, DY, ans)
print(ans)
print(p2)
