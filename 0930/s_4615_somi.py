import sys
sys.stdin= open('input.txt')


def put_stone(r, c, stone):

    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    if stone == 1: target = 2

    else: target = 1


    for di in range(8):
        can_reverse = []
        nr, nc = r + dr[di], c + dc[di]


        while True:
            if nr < 1 or nr > N or nc < 1 or nc > N or board[nr][nc] == 0:
                can_reverse = []
                break


            elif board[nr][nc] == stone:
                break

            else:
                can_reverse.append((nr, nc))
                nr += dr[di]
                nc += dc[di]

        for stones in can_reverse:
            x, y = stones
            board[x][y] = stone

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * (N + 2) for _ in range(N + 2)]

    center = N//2
    board[center][center], board[center + 1][center + 1] = 2, 2  # W 백돌
    board[center][center + 1], board[center + 1][center] = 1, 1  # B 흑돌

    for _ in range(M):
        c, r, stone = map(int, input().split())

        board[r][c] = stone
        put_stone(r, c, stone)


    B = 0
    W = 0
    for i in range(1, N + 1):
        B += board[i].count(1)
        W += board[i].count(2)

    print(B, W)
