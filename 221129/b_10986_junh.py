N, M = map(int, input().split())
A = list(map(int, input().split())) + [0]

dp = [0] * M

for i in range(N):
    num = (A[i-1] + A[i]) % M
    A[i] = num
    dp[num] += 1

answer = dp[0]
for num in dp:
    answer += num * (num - 1) // 2

print(answer)

