import os
from functools import cmp_to_key

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '13.in'))


def compare(x1, x2):
    if type(x1) == int and type(x2) == int:
        if x1 == x2:
            return 0
        elif x1 < x2:
            return -1
        else:
            return 1
    elif type(x1) == list and type(x2) == list:
        i = 0
        while i < len(x1) and i < len(x2):
            c = compare(x1[i], x2[i])
            if c == 1:
                return 1
            if c == -1:
                return -1
            i += 1
        if i == len(x1) and i < len(x2):
            return -1
        elif i < len(x1) and i == len(x2):
            return 1
        else:
            return 0
    elif type(x1) == list and type(x2) == int:
        return compare(x1, [x2])
    else:
        return compare([x1], x2)


def p1(S):
    nr = len(S) // 2
    idx = []
    for i in range(nr):
        s1, s2 = S[2*i], S[(2*i)+1]
        if compare(s1, s2) == -1:
            idx.append(i+1)
    return sum(idx)


def p2(S):
    packets = []
    for i in range(len(S)):
        packets.append(S[i])
    packets.append([[2]])
    packets.append([[6]])
    packets = sorted(packets, key=cmp_to_key(lambda x1, x2: compare(x1, x2)))
    idx = []
    for i, l in enumerate(packets):
        if l == [[2]] or l == [[6]]:
            idx.append(i+1)
    res = 1
    for i in idx:
        res *= i
    return res


if __name__ == '__main__':
    X = [eval(x.strip()) for x in open(FILE_PATH, 'r') if x != '\n']
    print(p1(X))
    print(p2(X))
