import sys

input = sys.stdin.readline
n, m = map(int, input().split())
names = [int(input()) for _ in range(n)]
dp = [float('inf')] * n

last_line = names[-1]
dp[-1] = 0
for i in range(n-2, -1, -1):
    last_line += 1 + names[i]
    if last_line <= m:
        dp[i] = 0
    else:
        break

for i in range(n-1, -1, -1):
    if not dp[i]: continue
    now = names[i]
    dp[i] = min(dp[i], (m-now) ** 2 + dp[i+1])

    for j in range(i + 1, n):
        if now + 1 + names[j] > m:
            break
        now += 1 + names[j]
        dp[i] = min(dp[i], (m - now) ** 2 + dp[j+1])

print(dp[0])

'''
6 10
1   4 + 16
4   16 + 16
1   4
1   16
4   36
8
'''