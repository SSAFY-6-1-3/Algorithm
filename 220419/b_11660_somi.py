import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + arr[i][j]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - (dp[x1 - 1][y2] + dp[x2][y1 - 1] - dp[x1 - 1][y1 - 1]))

# 시간초과
'''
def get_sum(x1, y1, x2, y2):
    area_sum = 0
    for r in range(x1-1, x2):
        for c in range(y1-1, y2):
            area_sum += arr[r][c]
    return area_sum


N, M = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(get_sum(x1, y1, x2, y2))

'''
