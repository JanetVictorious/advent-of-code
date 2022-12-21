import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '15.in'))


def dist(pnt1, pnt2):
    x1, y1 = pnt1
    x2, y2 = pnt2
    return abs(x1 - x2) + abs(y1 - y2)


def x_min_max(pnt1, row, dist):
    x1, y1 = pnt1
    x_diff = dist - abs(y1 - row)
    x_min = x1 - x_diff
    x_max = x1 + x_diff
    return x_min, x_max


def valid(x, y, S):
    for s in S:
        z1, b1 = s
        md = dist(z1, b1)
        d = abs(x - z1[0]) + abs(y - z1[1])
        if d <= md:
            return False
    return True


def p1(S, part=1, row=10, max_val=20):
    B = set()
    R = set()
    found = False
    for s in S:
        z1, b1 = s
        md = dist(z1, b1)
        B.add(tuple(b1))
        if part == 1 and z1[1] - md <= row <= z1[1] + md:
            x_min, x_max = x_min_max(z1, row, md)
            for i in range(x_min, x_max+1):
                if (i, row) not in B:
                    R.add((i, row))
        elif part == 2 and not found:
            for di in range(md+2):
                dj = (md+1) - di
                for dii, djj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    x = z1[0] + (di * dii)
                    y = z1[1] + (dj * djj)
                    if not (0 <= x <= max_val and 0 <= y <= max_val):
                        continue
                    if valid(x, y, S) and not found:
                        val = x * 4000000 + y
                        found = True

    if part == 1:
        nr_pnts = len(R)
        return nr_pnts
    elif part == 2:
        return val


if __name__ == '__main__':
    X = [x.strip().split(':') for x in open(FILE_PATH, 'r')]
    XS = []
    x_min, x_max = 0, 0
    y_min, y_max = 0, 0
    for x in X:
        x1, y1 = x
        xx1, xx2 = x1.split(',')
        yy1, yy2 = y1.split(',')
        xx1 = int(xx1.replace('Sensor at x=', '').strip())
        xx2 = int(xx2.replace('y=', '').strip())
        yy1 = int(yy1.replace('closest beacon is at x=', '').strip())
        yy2 = int(yy2.replace('y=', '').strip())
        XS.append([[xx1, xx2], [yy1, yy2]])
        x_min, x_max = min(x_min, min(xx1, yy1)), max(x_max, max(xx1, yy1))
        y_min, y_max = min(y_min, min(xx2, yy2)), max(y_max, max(xx2, yy2))
    print(p1(XS, row=2000000))
    print(p1(XS, part=2, max_val=4000000))
