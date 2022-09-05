import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '04.in'))


def p1(draw_nums, boards, res_boards):
    def _loop():
        """Closure to easier break loop."""
        for d in draw_nums:
            for b, r, idx in zip(boards, res_boards, range(len(boards))):
                for i in range(5):
                    for j in range(5):
                        r[i][j] = 1 if b[i][j] == d or r[i][j] == 1 else 0
                        if sum(r[i]) == 5 or sum([r2[j] for r2 in r]) == 5:
                            print('BINGO!')
                            return d, idx

    d, idx = _loop()
    board = boards[idx]
    res_board = res_boards[idx]
    res_val = 0
    for i in range(5):
        for j in range(5):
            if res_board[i][j] == 1:
                continue
            res_val += board[i][j]

    return d * res_val


def p2(draw_nums, boards, res_boards):
    def _loop():
        bingos = {}
        for d in draw_nums:
            for b, r, idx in zip(boards, res_boards, range(len(boards))):
                for i in range(5):
                    for j in range(5):
                        r[i][j] = 1 if b[i][j] == d or r[i][j] == 1 else 0
                        if sum(r[i]) == 5 or sum([r2[j] for r2 in r]) == 5:
                            if not bingos.get(idx):
                                bingos[idx] = True
                                last_idx = idx
                                last_d = d
                                if len(boards) == len(bingos):
                                    print('LAST BINGO!')
                                    return last_d, last_idx

    d, idx = _loop()
    board = boards[idx]
    res_board = res_boards[idx]
    res_val = 0
    for i in range(5):
        for j in range(5):
            if res_board[i][j] == 1:
                continue
            res_val += board[i][j]

    return d * res_val


if __name__ == '__main__':
    # Read input data
    X = [x.strip() for x in open(FILE_PATH, 'r')]
    draws = [int(i) for i in X[0].split(',')]
    res_boards = []
    boards = []
    board = []
    for line in X[1:]:
        if line:
            board.append([int(i) for i in line.split()])
        else:
            if board:
                boards.append(board)
            board = []
    boards.append(board)

    # Validate boards are on size 5x5 and construct results board
    for b in boards:
        assert len(b) == 5 and len(b[0]) == 5
        res_boards.append([[0 for _ in range(5)] for _ in range(5)])

    print(p1(draws, boards, res_boards))

    # Reset results board
    res_boards = []
    for b in boards:
        res_boards.append([[0 for _ in range(5)] for _ in range(5)])
    print(p2(draws, boards, res_boards))
