import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '02.in'))


def p1(pos, mag):
    x, y = 0, 0
    x = sum([v for p, v in zip(pos, mag) if p == 'forward'])
    y = sum([v for p, v in zip(pos, mag) if p == 'down']) - sum([v for p, v in zip(pos, mag) if p == 'up'])  # noqa: E501

    return x * y


def p2(pos, mag):
    aim, hor, dep = 0, 0, 0
    for p, m in zip(pos, mag):
        if p == 'forward':
            hor += m
            dep += m * aim
        elif p == 'down':
            aim += m
        else:
            aim -= m
    return hor * dep


if __name__ == '__main__':
    pos, mag = [], []
    for line in open(FILE_PATH, 'r'):
        x, y = line.split()
        pos.append(x)
        mag.append(int(y))
    print(p1(pos, mag))
    print(p2(pos, mag))
