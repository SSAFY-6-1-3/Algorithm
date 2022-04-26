N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for x in range(N):                      # 아래, 오른쪽으로만 이동 가능하므로
    for y in range(N):
        if x == N-1 and y == N-1:
            break
        if dp[x][y] > 0:
            num = board[x][y]
            if x+num in range(N):
                    dp[x+num][y] += dp[x][y]
            if y+num in range(N):
                dp[x][y + num] += dp[x][y]

print(dp[-1][-1])
