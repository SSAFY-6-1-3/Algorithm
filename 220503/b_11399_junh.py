N = int(input())
li = sorted(map(int, input().split()))
dp = [0]*N
dp[0] = li[0]
for i in range(1, N):
    dp[i] = dp[i-1] + li[i]

print(sum(dp))