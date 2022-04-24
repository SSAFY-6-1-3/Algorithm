# N, M = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# lst = [list(map(int, input().split())) for _ in range(M)]
# dp = [[0] * N for _ in range(N)]
#
# for i in range(N):
#     for j in range(N):
#         dp[i][j] = matrix[i][j]
#         if i-1 in range(N) and j-1 in range(N):
#             dp[i][j] -= dp[i-1][j-1]
#         if i-1 in range(N):
#             dp[i][j] += dp[i-1][j]
#         if j-1 in range(N):
#             dp[i][j] += dp[i][j-1]
#
# for s1, e1, s2, e2 in lst:
#     s1 -= 1
#     e1 -= 1
#     s2 -= 1
#     e2 -= 1
#     ans = dp[s2][e2]
#     if s1-1 in range(N):
#         ans -= dp[s1-1][e2]
#     if e1-1 in range(N):
#         ans -= dp[s2][e1-1]
#     if s1-1 in range(N) and e1-1 in range(N):
#         ans += dp[s1-1][e1-1]
#     print(ans)

#########################################################
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
lst = [list(map(int, input().split())) for _ in range(M)]
dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = matrix[i][j] + dp[i+1][j] + dp[i][j+1] - dp[i][j]

for s1, e1, s2, e2 in lst:
    ans = dp[s2][e2] - dp[s1-1][e2] - dp[s2][e1-1] + dp[s1-1][e1-1]
    print(ans)