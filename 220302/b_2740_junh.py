

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

answer = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for m in range(M):
            answer[i][j] += A[i][m] * B[m][j]

for i in range(N):
    print(*answer[i])






