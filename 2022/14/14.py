import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '14.in'))


def rock(points):
    nr_lines = len(points) - 1
    max_y = 0
    for i in range(nr_lines):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        max_y = max(max_y, y1, y2)
        if x1 == x2:
            min_y = min(y1, y2)
            for j in range(abs(y1 - y2) + 1):
                R.add((x1, min_y+j))
        else:
            min_x = min(x1, x2)
            for j in range(abs(x1 - x2) + 1):
                R.add((min_x+j, y1))
    return max_y


def units(x, y, count=0):
    prev = (x, y)
    next = (x, y+1)
    next_l = (x-1, y+1)
    next_r = (x+1, y+1)
    if count > 800:
        return 0
    elif next not in Z and next not in R:
        return units(x, y+1, count+1)
    else:
        if prev not in Z:
            if next_l not in Z and next_l not in R:
                return units(x-1, y+1, count+1)
            elif next_r not in Z and next_r not in R:
                return units(x+1, y+1, count+1)
            else:
                Z.add(prev)
                return 1


def p1(S, part=1):
    global Z
    global R
    Z = set()
    R = set()
    max_y = 0
    for lines in S:
        y = rock(lines)
        max_y = max(max_y, y)
    max_y += 2
    if part == 2:
        for i in range(1000):
            R.add((i, max_y))
    u = 0
    while True:
        unit = units(500, 0)
        if unit == 0 or unit is None:
            break
        u += unit
    return u


if __name__ == '__main__':
    X = [x.strip().split('->') for x in open(FILE_PATH, 'r')]
    XS = [[y.strip().split(',') for y in xs] for xs in X]
    print(p1(XS))
    print(p1(XS, part=2))
