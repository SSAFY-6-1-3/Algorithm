R, C, T = map(int, input().split())
mat = []
up = None
for i in range(R):
    line = list(map(int, input().split()))
    for j in range(C):
        if line[j] == -1:
            if not up:
                up = (i, j)
    mat.append(line)

dY = (-1, 0, 1, 0)
dX = (0, 1, 0, -1)


def spread():
    new_mat = [[0]*C for _ in range(R)]
    new_mat[up[0]][up[1]] = -1
    new_mat[up[0] + 1][up[1]] = -1

    for y in range(R):
        for x in range(C):
            if mat[y][x] > 0:
                cnt = 0
                for d in range(4):
                    ny, nx = y + dY[d], x + dX[d]
                    if ny not in range(R) or nx not in range(C) or mat[ny][nx] == -1:
                        continue
                    cnt += 1
                    new_mat[ny][nx] += mat[y][x] // 5

                new_mat[y][x] += mat[y][x] - (mat[y][x]//5) * cnt    # 소수점 버리는거 맞는지 체크
    return new_mat


def clean(is_up):
    y_s = 0 if is_up else up[0] + 1
    y_e = up[0] + 1 if is_up else R
    d = 0 + (not is_up) * 2
    y, x = up[0] + dY[d] + (not is_up), up[1] + dX[d]
    while True:
        ny, nx = y + dY[d], x + dX[d]
        if ny not in range(y_s, y_e) or nx not in range(C):
            d = (d + 1 - 2 * (not is_up)) % 4
            continue
        elif mat[ny][nx] == -1:
            mat[y][x] = 0
            break
        mat[y][x] = mat[ny][nx]
        y, x = ny, nx


for _ in range(T):
    mat = spread()
    clean(True)
    clean(False)

print(sum(sum(i) for i in mat) + 2)




