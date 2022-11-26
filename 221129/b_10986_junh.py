import copy

N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-1] * M for _ in range(N)]

answer = 0
num = 0

for i in range(N):
    num = (num + A[i]) % M
    if num == 0:
        answer += 1
    dp[num] = answer

# for i in range(1, N):
#     tmp = [0] * N
#     for j in range(i, N):
#         tmp[j] = (dp[j] - A[i-1]) % M
#         if tmp[j] == 0:
#             answer += 1
#     dp = tmp
print(dp)
print(answer)

