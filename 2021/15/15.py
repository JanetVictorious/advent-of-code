import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, 'test.in'))


def p1(n):
    start = (0, 0, 0)
    end = (n * R - 1, n * C - 1)

    D = [[None for _ in range(n * C)] for _ in range(n * R)]
    Q = [(start)]


if __name__ == '__main__':
    # Parse input data
    X = [list(map(int, list(x.strip()))) for x in open(FILE_PATH, 'r')]

    R = range(X)
    C = range(X[0])

    DR = [-1, 0, 1, 0]
    DC = [0, 1, 0, -1]

    print(p1(X))
