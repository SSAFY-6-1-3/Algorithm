N = int(input())
miro = list(map(int, input().split()))
dp = [1001] * len(miro)  # jump 횟수
dp[0] = 0

for i in range(len(miro)):
    for j in range(1, miro[i] + 1):
        if i + j <= len(miro) - 1:
            dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[-1] == 1001:
    print(-1)
else:
    print(dp[-1])
