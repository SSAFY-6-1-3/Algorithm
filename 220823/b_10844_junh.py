
N = int(input())
dp = [1] * 10

for _ in range(N-1):
    tmp = [0] * 10

    tmp[0] = dp[1] % 1000000000
    tmp[9] = dp[8] % 1000000000
    for i in range(1, 9):
        tmp[i] = (dp[i-1] + dp[i+1]) % 1000000000

    dp = tmp[:]

print(sum(dp[1:]) % 1000000000)