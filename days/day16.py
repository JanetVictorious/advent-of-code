import os
import numpy as np

base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, '..', 'data/day16.csv'))

hex = np.genfromtxt(file_path, dtype=str).reshape(1)[0]

# hex = 'D2FE28'

binary = bin(int(hex, 16))[2:]

while len(binary) < 4 * len(hex):
    binary = '0' + binary

assert len(binary) % 4 == 0
assert len(binary) == 4 * len(hex)

p1 = 0


def solve(bits, i, indent):
    global p1
    ver = int(bits[(i + 0):(i + 3)], 2)
    p1 += ver
    typ = int(bits[(i + 3):(i + 6)], 2)

    if typ == 4:
        i += 6
        v = 0
        while True:
            v = v * 16 + int(bits[(i + 1):(i + 5)], 2)
            i += 5
            if bits[i - 5] == '0':
                return v, i
    else:
        len_id = int(bits[i+6], 2)
        vs = []
        if len_id == 0:
            len_bits = int(bits[(i + 7):(i + 7 + 15)], 2)
            start_i = i + 7 + 15
            i = start_i
            while True:
                v, next_i = solve(bits, i, indent + 1)
                vs.append(v)
                assert next_i > i
                assert next_i - start_i <= len_bits
                i = next_i
                if next_i - start_i == len_bits:
                    break
        else:
            n_packets = int(bits[(i + 7):(i + 7 + 11)], 2)
            i += 7 + 11
            for t in range(n_packets):
                v, next_i = solve(bits, i, indent + 1)
                vs.append(v)
                assert next_i > i
                i = next_i
        if typ == 0:
            return sum(vs), i
        elif typ == 1:
            ans = 1
            for v in vs:
                ans *= v
            return ans, i
        elif typ == 2:
            return min(vs), i
        elif typ == 3:
            return max(vs), i
        elif typ == 5:
            return (1 if vs[0] > vs[1] else 0), i
        elif typ == 6:
            return (1 if vs[0] < vs[1] else 0), i
        elif typ == 7:
            return (1 if vs[0] == vs[1] else 0), i
        else:
            assert False, typ


# +------------------+
# |   Puzzle 1 + 2   |
# +------------------+

value, next_i = solve(binary, 0, 0)
assert len(binary) - 4 < next_i <= len(binary)
print(p1)
print(value)
