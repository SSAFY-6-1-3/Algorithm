import sys

input = sys.stdin.readline

def make_dp(N):
    for n in range(3, N+1):
        dp[n] = max(dp[n-2], dp[n-3]+stair[n-1])+stair[n]


N = int(input())
stair = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)
dp[1] = stair[1]
if N >1:
    dp[2] = stair[1] + stair[2]
make_dp(N)
print(dp[N])
