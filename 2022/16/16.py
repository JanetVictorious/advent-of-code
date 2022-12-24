import os
from collections import deque

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '16.in'))


def simulate(path1, valves1, path2, valves2, D):
    V1, V2 = deque(valves1), deque(valves2)
    v_1, v_2 = V1.popleft(), V2.popleft()
    res = 0
    open_v = set()
    P1, P2 = deque(path1), deque(path2)
    p_1, p_2 = 'AA', 'AA'
    for _ in range(26):
        for o in open_v:
            res += D[o]['rate']
        p_1 = P1.popleft() if len(P1) > 1 else p_1
        p_2 = P2.popleft() if len(P2) > 1 else p_2
        if p_1 == v_1 and v_1 not in open_v:
            open_v.add(p_1)
            v_1 = V1.popleft() if len(V1) > 1 else v_1
            P1 = deque([p_1]) + P1
        if p_2 == v_2 and v_2 not in open_v:
            open_v.add(p_2)
            v_2 = V2.popleft() if len(V2) > 1 else v_2
            P2 = deque([p_2]) + P2
    return res


def p1(S):
    start = ('AA', 0, 0, [], deque())
    Q = deque([start])
    res1 = set()
    max_rate = 0
    valves = set([i for i, j in S.items() if j['rate'] > 0])
    res2 = []
    while Q:
        pos, time, rate, prev, open_valves = Q.popleft()
        if time == 30:
            res1.add(rate)
            continue
        to_open = S[pos]['rate'] > 0 and pos not in open_valves
        if abs(max_rate - rate) > 140:
            continue
        for o in open_valves:
            rate += S[o]['rate']
        max_rate = max(max_rate, rate)
        ov = deque(open_valves)
        if to_open:
            ov.append(pos)
            Q.append((pos, time + 1, rate, prev, ov))
        else:
            if len(ov) == len(valves) // 2 + 1:
                res2.append([time, rate, prev, ov])
            elif len(ov) == len(valves):
                Q.append((pos, time + 1, rate, prev, ov))
                continue
            for i in S[pos]['valves']:
                Q.append((i, time + 1, rate, prev + [pos], ov))

    result1 = max(res1)
    res2_adj = [i for i in res2 if i[0] < 15]
    part2 = [0]
    cache = dict()
    for i in range(len(res2_adj)):
        cache[i] = dict()
        for j in range(len(res2_adj)):
            if i == j:
                continue
            if cache.get(j):
                if cache.get(j).get(i):
                    continue
            if list(res2_adj[i][3])[1:] == list(res2_adj[j][3])[0:-1]:
                continue
            s = simulate(res2_adj[i][2], res2_adj[i][3], res2_adj[j][2], res2_adj[j][3], S)
            cache[i][j] = s
            if s == 0:
                continue
            part2.append(s)
    result2 = max(part2)

    return result1, result2


if __name__ == '__main__':
    X = [x.strip().split(';') for x in open(FILE_PATH, 'r')]
    XS = dict()
    for x in X:
        x1, x2 = x
        x11, x12 = x1.split('=')
        x11, x12 = x11[6:8], int(x12)
        if 'tunnels lead to valves' in x2:
            x2 = x2.replace('tunnels lead to valves', '').strip()
            x2s = x2.split(',')
        elif 'tunnel leads to valve' in x2:
            x2 = x2.replace('tunnel leads to valve', '').strip()
            x2s = [x2]
        x2s = [x.strip() for x in x2s]
        XS[x11] = dict()
        XS[x11]['rate'] = x12
        XS[x11]['valves'] = x2s
    print(p1(XS))
