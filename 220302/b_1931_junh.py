import sys
input = sys.stdin.readline

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]

li.sort(key= lambda x:(x[1], x[0]))

dp = [1] * N
best = 0
for i in range(1, N):
    if li[best][1] <= li[i][0]:
        dp[i] = dp[best]+1
        best = i

print(dp[best])