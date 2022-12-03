import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
board =[" " * (M+1)] + ['_' + input() for _ in range(N)]
cnts = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        cnts[i][j] = cnts[i-1][j] + cnts[i][j-1] - cnts[i-1][j-1]

        if (i + j) % 2 == 0 and board[i][j] == 'B':
            cnts[i][j] += 1
        elif (i + j) % 2 == 1 and board[i][j] == 'W':
            cnts[i][j] += 1

answer = K ** 2
for i in range(1, N - K + 2):
    for j in range(1, M - K + 2):
        ans = cnts[i + K - 1][j + K - 1] - cnts[i + K - 1][j - 1] - cnts[i - 1][j + K - 1] + cnts[i - 1][j - 1]
        answer = min(answer, ans, K ** 2 - ans)

print(answer)