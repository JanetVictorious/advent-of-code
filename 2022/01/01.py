import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '01.in'))


def p1(S, top=1):
    values = []
    value = 0
    for s in S:
        if s == b'':
            values.append(value)
            value = 0
            continue
        value += int(s)
    values.sort()
    return sum(values[-top:])


if __name__ == '__main__':
    X = [x.strip() for x in open(FILE_PATH, 'rb')]
    print(p1(X))
    print(p1(X, top=3))
