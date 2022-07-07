
N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    t, p = li[i]

    if i+t in range(0, N+1):
        dp[i] = max(dp[i], dp[i+t] + p)
    dp[i] = max(dp[i], dp[i+1])

print(dp[0])