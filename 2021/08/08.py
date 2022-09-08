import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '08.in'))


def p1(S):
    sep = False
    cnt = 0
    for s in S:
        for x in s:
            if sep:
                if len(x) in [2, 3, 4, 7]:
                    cnt += 1
            if x == '|':
                sep = True
        sep = False
    return cnt


def p2(S):
    prod = 0
    for s in S:
        d, D = {}, {}
        d[5], d[6] = [], []
        to_code = []
        sep = False
        for x in s:
            if sep:
                to_code.append(x)
            elif x == '|':
                sep = True
            elif len(x) == 2:
                d[1] = x
            elif len(x) == 3:
                d[7] = x
            elif len(x) == 4:
                d[4] = x
            elif len(x) == 5:
                d[5].append(x)
            elif len(x) == 6:
                d[6].append(x)
            elif len(x) == 7:
                d[8] = x

        # Deduce numbers set
        D[1] = set(d[1])
        D[4] = set(d[4])
        D[7] = set(d[7])
        D[8] = set(d[8])
        for i in d[5]:
            if len(set(d[1]).intersection(set(i))) == 2:
                D[3] = set(i)
            elif len(set(d[4]).intersection(set(i))) == 2:
                D[2] = set(i)
            elif len(set(d[4]).intersection(set(i))) == 3:
                D[5] = set(i)
        for i in d[6]:
            if len(D[3].intersection(set(i))) == 5:
                D[9] = set(i)
            elif len(D[5].intersection(set(i))) == 5:
                D[6] = set(i)
            else:
                D[0] = set(i)

        num_str = ''
        for d in to_code:
            for i, s in D.items():
                if set(s) == set(d):
                    num_str += str(i)

        prod += int(num_str)

    return prod


if __name__ == '__main__':
    # Parse input data
    XS = [x for x in open(FILE_PATH, 'r')]
    X = [x.split() for x in XS]

    print(p1(X))
    print(p2(X))
