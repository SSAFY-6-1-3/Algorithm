N, K = map(int, input().split())
dY = (0, 0, -1, 1)
dX = (1, -1, 0, 0)

colors = [list(map(int, input().split())) for _ in range(N)]
mat = [[[] for _ in range(N)] for _ in range(N)]
units = []

for i in range(K):
    y, x, d = map(int, input().split())
    y, x, d = y-1, x-1, d-1
    mat[y][x].append(i)
    units.append([y, x, d])


def solve():
    turn = 0
    while turn < 1001:
        turn += 1
        i = 0
        blued = False    # 파란색 체크용

        while i < K:
            y, x, d = units[i]
            idx = mat[y][x].index(i)
            nums = mat[y][x][idx:]
            ny, nx = y + dY[d], x + dX[d]

            if ny not in range(N) or nx not in range(N) or colors[ny][nx] == 2:
                if not blued:
                    d = d // 2 * 2 + (d % 2 + 1) % 2
                    units[i][2] = d
                    blued = True
                    continue
                else:
                    pass
            else:
                if colors[ny][nx] == 1:
                    nums = nums[::-1]
                mat[ny][nx].extend(nums)
                if len(mat[ny][nx]) >= 4:
                    return turn
                for num in nums:
                    units[num][0] = ny
                    units[num][1] = nx
                mat[y][x] = mat[y][x][:idx]

            blued = False
            i += 1
    return -1

print(solve())