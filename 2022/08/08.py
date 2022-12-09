import os
import numpy as np

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '08.in'))


def p1(S):
    n_x, n_y = S.shape

    Z = set()
    max_score = 0.0
    for x in range(1, n_x-1):
        for y in range(1, n_y-1):
            if (x, y) not in Z:
                if S[x, y] == 0:
                    continue
                score = 1.0
                for i in range(2):
                    if i == 0:
                        x2 = S[0:x, y]
                        y2 = S[x, 0:y]
                    else:
                        x2 = S[x+1:, y]
                        y2 = S[x, y+1:]
                    if all(x2 < S[x, y]) or all(y2 < S[x, y]):
                        Z.add((x, y))
                        cnt_x = 0
                        cnt_y = 0
                        for j1 in reversed(x2) if i == 0 else x2:
                            if j1 < S[x, y]:
                                cnt_x += 1
                            else:
                                cnt_x += 1
                                break
                        score *= cnt_x

                        for j2 in reversed(y2) if i == 0 else y2:
                            if j2 < S[x, y]:
                                cnt_y += 1
                            else:
                                cnt_y += 1
                                break
                        score *= cnt_y
                max_score = max([max_score, score])

    ins = len(Z)
    vsb = ins + n_x*2 + (n_y-2)*2

    return vsb, max_score


if __name__ == '__main__':
    X = [list(x.strip()) for x in open(FILE_PATH, 'r')]
    X = [[int(y) for y in x] for x in X]
    X2 = np.array(X).reshape(len(X), len(X[0]))
    print(p1(X2))
