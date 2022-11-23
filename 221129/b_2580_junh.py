
board = [list(map(int, input().split())) for _ in range(9)]
blanks = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blanks.append((i, j))

def check(y, x):
    n = board[y][x]
    by, bx = y // 3 * 3, x // 3 * 3

    for i in range(3):
        for j in range(3):
            num = i * 3 + j
            if num != y and board[num][x] == n:
                return False
            if num != x and board[y][num] == n:
                return False
            if (by+i != y or bx + j != x) and board[by + i][bx + j] == n:
                return False
    return True


def rec(idx):
    y, x = blanks[idx]
    if idx == len(blanks) - 1:
        for i in range(1, 10):
            board[y][x] = i
            if check(y, x):
                for line in board:
                    print(*line)
                exit()
    else:
        for i in range(1, 10):
            board[y][x] = i
            if check(y, x):
                rec(idx + 1)
        board[y][x] = 0


rec(0)