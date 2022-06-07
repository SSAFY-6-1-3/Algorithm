import sys

input = sys.stdin.readline

T = int(input())
Ns = [int(input()) for _ in range(T)]

dp = [1] * max(Ns)

for i in range(3, max(Ns)):
    dp[i] = dp[i-2] + dp[i-3]

for N in Ns:
    print(dp[N-1])
