N = int(input())
miro = list(map(int, input().split()))
dp = [100001] * N
dp[0] = 0
for idx in range(N):
    for num in range(1, miro[idx]+1):
        if idx + num in range(N):
            dp[idx+num] = min(dp[idx+num], dp[idx]+1)
if dp[-1] == 100001:
    print(-1)
else:
    print(dp[-1])