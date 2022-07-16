
N = int(input())
li = list(map(int, input().split()))

dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if li[i] > li[j] and dp[j]+1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))


a = [1, 2, 3, 1, 2, 3, 4]