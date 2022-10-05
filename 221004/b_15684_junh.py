
N, M, H = map(int, input().split())
mat = [[0]*H for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    mat[a-1][b-1] = 1
    mat[a-1][b] = -1


print(mat)
