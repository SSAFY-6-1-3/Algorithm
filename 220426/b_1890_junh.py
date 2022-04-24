N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp [0][0] = 1
for i in range(N):
    for j in range(N):
        n = mat[i][j]
        if not n: break
        if i+n in range(N):
            dp[i+n][j] += dp[i][j]
        if j+n in range(N):
            dp[i][j+n] += dp[i][j]
print(dp[N-1][N-1])