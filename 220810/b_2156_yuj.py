# dp[i]에서 비교해야할 경우
# i-2 i-2 i
#  x   o  o
#  o   x  o
#  x   x  o

n = int(input())
grapes = list(int(input()) for _ in range(n))
dp = [0] * n
dp[0] = grapes[0]
if n > 1:
    dp[1] = grapes[0] + grapes[1]

if n > 2:
    dp[2] = max(grapes[1] + grapes[2], dp[0] + grapes[2], dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i-3] + grapes[i-1] + grapes[i], dp[i-2] + grapes[i], dp[i-1])

print(max(dp))