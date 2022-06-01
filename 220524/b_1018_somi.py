def check_cnt(r, c, ansboard):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if board[r + i][c + j] != ansboard[i][j]:
                cnt += 1
    return cnt


N, M = map(int, input().split())
board = list(list(input()) for _ in range(N))

WB = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
BW = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

W_board = [WB, BW, WB, BW, WB, BW, WB, BW]
B_board = [BW, WB, BW, WB, BW, WB, BW, WB]
ans = N * M

for r in range(N - 7):
    for c in range(M - 7):

        ans = min(ans, check_cnt(r, c, W_board))
        ans = min(ans, check_cnt(r, c, B_board))
print(ans)