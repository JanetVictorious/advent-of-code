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


# +--------------+
# |   Puzzle 1   |
# +--------------+

p1 = 10 - 1
p2 = 7 - 1

s1 = 0
s2 = 0
roll = 0

while True:
    m1 = dice_val(dice_vals)
    roll += 3
    p1 = (p1 + m1) % 10
    s1 += p1 + 1

    if s1 > 1000:
        break

    m2 = dice_val(dice_vals)
    roll += 3
    p2 = (p2 + m2) % 10
    s2 += p2 + 1

    if s2 > 1000:
        break

print(min([s1, s2]) * roll)

# +--------------+
# |   Puzzle 2   |
# +--------------+

p1 = 10 - 1
p2 = 7 - 1
DP = {}  # game state -> answer for that game state


def count_win(p1, p2, s1, s2):
    # Given that A is at position p1 with score s1, and B is at position p2
    # with score s2, and A is to move, return (# of universes where player A
    # wins, # of universes where player B wins)
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
