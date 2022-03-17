T = int(input())
dp = [0]*11
dp[0]= 1
for i in range(1, 11):
    for j in range(1, 4):
        if i-j>=0:
            dp[i] += dp[i-j]

for _ in range(T):
    n = int(input())
    print(dp[n])