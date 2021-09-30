import sys

sys.stdin = open('s_4615.txt')

MOVES = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def change(y, x, clr, move, inverted):
    ny, nx = y + move[0], x + move[1]
    if ny not in range(N+1) or nx not in range(N+1) or not board[ny][nx]:
        return False
    changed = False
    if board[ny][nx] == -clr:
        changed = change(ny, nx, clr, move, True)
    elif inverted and board[ny][nx] == clr:
        changed = True

    if changed:
        board[y][x] = clr
    return changed


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N+1)] for _ in range(N+1)]
    h = N//2
    board[h][h], board[h+1][h], board[h][h+1], board[h+1][h+1] = 1, -1, -1, 1

    for _ in range(M):
        y, x, clr = map(int, input().split())
        clr = clr*2 -3
        board[y][x] = clr
        # if start_check(y, x, clr):
        for move in MOVES:
            change(y, x, clr, move, False)
    blk, wht = 0, 0
    for y in range(N+1):
        for x in range(N+1):
            if board[y][x] == -1:
                blk += 1
            elif board[y][x] == 1:
                wht += 1
    print('#{} {} {}'.format(tc, blk, wht))