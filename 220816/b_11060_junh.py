
N = int(input())
li = list(map(int, input().split()))
dp = [1001] * N
dp[0] = 0
for i in range(N):
    for j in range(1, li[i]+1):
        if i + j < N:
            dp[i+j] = min(dp[i+j], dp[i] + 1)

if dp[-1] == 1001:
    print(-1)
else:
    print(dp[-1])