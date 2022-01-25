import sys

input = sys.stdin.readline

def check_dp(n):
    dp = [[0]*i for i in range(1, n+1)]
    dp[0] = tri[0]
    for i in range(n-1):
        for j in range(i+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+tri[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+tri[i+1][j+1])
    return max(dp[n-1])

n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

print(check_dp(n))