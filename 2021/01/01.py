import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '01.in'))


def p1(x):
    c = 0
    for i in range(0, len(x)-1):
        if x[i+1] > x[i]:
            c += 1
    return c


def p2(x):
    c = 0
    for i in range(1, len(x)-2):
        k = i + 1
        if sum(x[k-1:k+2]) > sum(x[i-1:i+2]):
            c += 1
    return c


if __name__ == '__main__':
    X = [int(x) for x in open(FILE_PATH, 'rb')]
    print(p1(X))
    print(p2(X))
