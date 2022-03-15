dp = [0] * (10**6+1)
for n in range(2, 10**6+1):
    if not n % 6:
        dp[n] = min(dp[n-1]+1, dp[n//3]+1, dp[n//2]+1)
    elif not n % 3:
        dp[n] = min(dp[n-1]+1, dp[n//3]+1)
    elif not n % 2:
        dp[n] = min(dp[n-1]+1, dp[n//2]+1)
    else:
        dp[n] = dp[n-1]+1
print(dp[int(input())])