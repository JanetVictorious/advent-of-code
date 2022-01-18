import os

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day22.in'))

data = open(file_path).read().strip()

data = data.split('\n')

steps = []
coord = []
for line in data:
    step, coords = line.strip().split(' ')
    steps.append(step)
    coord.append(coords)

C = []
for line in coord:
    x_r, y_r, z_r = line.strip().split(',')
    x_min, x_max = [int(x) for x in x_r.replace('x=', '').split('..')]
    y_min, y_max = [int(x) for x in y_r.replace('y=', '').split('..')]
    z_min, z_max = [int(x) for x in z_r.replace('z=', '').split('..')]
    C.append(((x_min, x_max), (y_min, y_max), (z_min, z_max)))

C = [((2, 5), (1, 4)), ((3, 7), (3, 6)), ((4, 6), (5, 7))]

G = set()
for c in C:
    print(c)
