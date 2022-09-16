
dY = (-1, -1, -1, 0, 0, 1, 1, 1)
dX = (-1, 0, 1, -1, 1, -1, 0, 1)

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
mat = [[[] for _ in range(N)] for _ in range(N)]
biryo = [[5]*N for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    mat[x-1][y-1].append(z)


def spr_smr():
    for y in range(N):
        for x in range(N):
            mat[y][x].sort()
            for z in range(len(mat[y][x])):
                if mat[y][x][z] > biryo[y][x]:
                    for dead in mat[y][x][z:]:
                        biryo[y][x] += dead // 2
                    mat[y][x] = mat[y][x][:z]
                    break
                biryo[y][x] -= mat[y][x][z]
                mat[y][x][z] += 1


def fall():
    for y in range(N):
        for x in range(N):
            for z in range(len(mat[y][x])):
                if not mat[y][x][z] % 5:
                    for d in range(8):
                        ny, nx = y + dY[d], x + dX[d]
                        if ny in range(N) and nx in range(N):
                            mat[ny][nx].append(1)


def winter():
    for y in range(N):
        for x in range(N):
            biryo[y][x] += A[y][x]

def year():
    spr_smr()
    fall()
    winter()

for _ in range(K):
    year()

cnt = 0
for y in range(N):
    for x in range(N):
        cnt += len(mat[y][x])
print(cnt)