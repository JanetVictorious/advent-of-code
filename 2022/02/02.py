import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '02.in'))


def p1(S, part=1):
    val = 0
    for d1, d2 in S:
        v1 = D1.get(d1)
        v2 = D2.get(d2)

        if part == 2:
            v2 = {(1, 'X'): 3, (1, 'Y'): 1, (1, 'Z'): 2,
                  (2, 'X'): 1, (2, 'Y'): 2, (2, 'Z'): 3,
                  (3, 'X'): 2, (3, 'Y'): 3, (3, 'Z'): 1}[(v1, d2)]
        val += v2
        val += {(1, 1): 3, (1, 2): 6, (1, 3): 0,
                (2, 1): 0, (2, 2): 3, (2, 3): 6,
                (3, 1): 6, (3, 2): 0, (3, 3): 3}[(v1, v2)]

    return val


if __name__ == '__main__':
    X = [x.strip().split() for x in open(FILE_PATH, 'r')]
    D1 = {'A': 1,
          'B': 2,
          'C': 3}
    D2 = {'X': 1,
          'Y': 2,
          'Z': 3}
    print(p1(X))
    print(p1(X, part=2))
