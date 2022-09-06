import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '05.in'))


def p1(lst, diagonal=False):
    # Get min/max values for x/y
    x_min, x_max = 0, 0
    y_min, y_max = 0, 0
    for line in lst:
        x1, x2 = line[0][0], line[1][0]
        y1, y2 = line[0][1], line[1][1]
        if x1 < x_min or x2 < x_min:
            x_min = min([x1, x2])
        if x1 > x_max or x2 > x_max:
            x_max = max([x1, x2])
        if y1 < y_min or y2 < y_min:
            y_min = min([y1, y2])
        if y1 > y_max or y2 > y_max:
            y_max = max([y1, y2])

    # Calculate grid
    grid = [[0 for _ in range(x_min, x_max+1)] for _ in range(y_min, y_max+1)]
    for line in lst:
        x1, x2 = line[0][0], line[1][0]
        y1, y2 = line[0][1], line[1][1]
        if x1 == x2:
            for i in range(min([y1, y2]), max([y1, y2])+1):
                grid[i][x1] += 1
        elif y1 == y2:
            for i in range(min([x1, x2]), max([x1, x2])+1):
                grid[y1][i] += 1
        elif diagonal:
            if x1 < x2 and y1 < y2:
                for x, y in zip(range(x1, x2+1), range(y1, y2+1)):
                    grid[y][x] += 1
            elif x1 < x2 and y1 > y2:
                for x, y in zip(range(x1, x2+1), range(y1, y2-1, -1)):
                    grid[y][x] += 1
            elif x1 > x2 and y1 < y2:
                for x, y in zip(range(x1, x2-1, -1), range(y1, y2+1)):
                    grid[y][x] += 1
            else:
                for x, y in zip(range(x1, x2-1, -1), range(y1, y2-1, -1)):
                    grid[y][x] += 1
        else:
            continue

    # Calculate intersections
    cnt = 0
    for line in grid:
        for i in line:
            if i > 1:
                cnt += 1
    return cnt


if __name__ == '__main__':
    # Parse input
    X1 = [x.strip() for x in open(FILE_PATH, 'r')]
    X2 = [x.split('->') for x in X1]
    X3 = [[y.split(',') for y in x] for x in X2]
    XS = [[[int(z.strip()) for z in y] for y in x] for x in X3]
    print(p1(XS))
    print(p1(XS, diagonal=True))
