def is_sq(num):
    return int(num ** 0.5) ** 2 == num


n = int(input())
dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    if is_sq(i):
        dp[i] = 1  # 제곱수라면 1
    else:
        dp[i] = i

for j in range(2, n + 1):
    for k in range(1, int(j ** 0.5) + 1):  # 제곱근의 정수값 까지만
        dp[j] = min(dp[j], dp[k * k] + dp[j - k * k])

print(dp[n])
