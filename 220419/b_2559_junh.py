N, K = map(int, input().split())

li = list(map(int, input().split()))
max_t = -100*K
dp = [0]* N
dp[0] = sum(li[:K])

for i in range(1, N-K+1):
    dp[i] = dp[i-1]-li[i-1]+li[i+K-1]

print(max(dp[:N-K+1]))