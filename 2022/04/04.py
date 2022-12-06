import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '04.in'))


def p1(S):
    cnt1 = 0
    cnt2 = 0
    for s in S:
        s1 = set(range(int(s[0]), int(s[1]) + 1))
        s2 = set(range(int(s[2]), int(s[3]) + 1))
        s_int = s1.intersection(s2)
        if len(s_int) in [len(s1), len(s2)]:
            cnt1 += 1
        if s_int:
            cnt2 += 1
    return cnt1, cnt2


if __name__ == '__main__':
    X = [x.strip().replace('-', ',').split(',') for x in open(FILE_PATH, 'r')]
    print(p1(X))
