N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

C = [[0 for _ in range(K)] for _ in range(N)]

for r in range(N):
    for c in range(K):
        tmp = 0
        for i in range(M):
            tmp += A[r][i] * B[i][c]
        C[r][c] = tmp

for row in C:
    print(*row)



