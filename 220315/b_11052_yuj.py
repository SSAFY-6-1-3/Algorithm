N = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    temp = 0
    for k in range(1, N+1):
        if i-k >= 0:
            dp[i] = max(dp[i], dp[i-k]+cards[k])
print(dp[N])