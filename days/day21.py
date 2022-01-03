from collections import OrderedDict, deque, Counter
from itertools import permutations

pl1 = 10
pl2 = 7

dice_vals = deque([int(x) for x in range(1, 101)])


def dice_val(dice_vals):
    val = 0
    for t in range(3):
        v = dice_vals.popleft()
        val += v
        dice_vals.append(v)
    return val


P1 = deque()
pl1_pos = []
for i in range(1, 11):
    if i == pl1:
        pl1_pos.append((i, True))
    else:
        pl1_pos.append((i, False))

val = [x[0] for x in pl1_pos if x[1]][0]
A, B = pl1_pos[val - 1:], pl1_pos[:val - 1]
for i in A:
    P1.append(i)
for i in B:
    P1.append(i)

P2 = deque()
pl2_pos = []
for i in range(1, 11):
    if i == pl2:
        pl2_pos.append((i, True))
    else:
        pl2_pos.append((i, False))
val = [x[0] for x in pl2_pos if x[1]][0]
A, B = pl2_pos[val - 1:], pl2_pos[:val - 1]
for i in A:
    P2.append(i)
for i in B:
    P2.append(i)

# +--------------+
# |   Puzzle 1   |
# +--------------+

score1 = 0
score2 = 0
roll = 0

while True:
    pl1_val = dice_val(dice_vals)
    roll += 3
    for i in range(pl1_val):
        pos1, val1 = P1.popleft()
        val1 = False
        P1.append((pos1, val1))
    score1 += P1[0][0]

    if score1 >= 1000:
        break

    pl2_val = dice_val(dice_vals)
    roll += 3
    for i in range(pl2_val):
        pos2, val2 = P2.popleft()
        val2 = False
        P2.append((pos2, val2))
    score2 += P2[0][0]

    if score2 >= 1000:
        break

print(min([score1, score2]) * roll)

# +--------------+
# |   Puzzle 2   |
# +--------------+

p1 = 10-1
p2 = 7-1
DP = {}  # game state -> answer for that game state


def count_win(p1, p2, s1, s2):
    # Given that A is at position p1 with score s1, and B is at position p2 with score s2, and A is to move,
    # return (# of universes where player A wins, # of universes where player B wins)
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    if (p1, p2, s1, s2) in DP:
        return DP[(p1, p2, s1, s2)]

    ans = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                new_p1 = (p1 + d1 + d2 + d3) % 10
                new_s1 = s1 + new_p1 + 1

                x1, y1 = count_win(p2, new_p1, s2, new_s1)
                ans = (ans[0] + y1, ans[1] + x1)
    DP[(p1, p2, s1, s2)] = ans
    return ans


print(max(count_win(p1, p2, 0, 0)))
