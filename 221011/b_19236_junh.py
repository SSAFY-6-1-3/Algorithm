from collections import deque
from copy import deepcopy

mat = [[0]*4 for _ in range(4)]
dY = (-1, -1, 0, 1, 1, 1, 0, -1)
dX = (0, -1, -1, -1, 0, 1, 1, 1)
fishes = [(0, 0, 0)] * 17
for y in range(4):
    line = list(map(int, input().split()))
    for x in range(0, 8, 2):
        mat[y][x//2] = line[x]
        fishes[line[x]] = (y, x//2, line[x+1]-1)    # y, x, d

n = mat[0][0]
mat[0][0] = 0
fishes[0] = fishes[n]
fishes[n] = None


def fish_move(n):
    if fishes[n] is None:
        return
    y, x, d = fishes[n]
    d = d
    for _ in range(8):
        ny, nx = y + dY[d], x + dX[d]
        if ny not in range(4) or nx not in range(4) or mat[ny][nx] == 0:
            d = (d + 1) % 8
            continue
        tmp = mat[ny][nx]
        if tmp != -1:
            tmp_d = fishes[tmp][2]
            fishes[tmp] = (y, x, tmp_d)
            mat[y][x] = tmp
        else:
            mat[y][x] = -1
        mat[ny][nx] = n
        fishes[n] = (ny, nx, d)
        return


q = deque([(mat, fishes, n)])
answer = 0
while q:
    mat, fishes, point = q.popleft()
    answer = max(answer, point)
    for i in range(1, 17):
        fish_move(i)

    y, x, d = fishes[0]
    for m in range(1, 4):
        ny, nx = y + dY[d] * m, x + dX[d] * m
        if ny not in range(4) or nx not in range(4):
            break
        elif mat[ny][nx] == -1:
            continue
        tmp_mat, tmp_fishes = deepcopy(mat), deepcopy(fishes)
        tmp_mat[ny][nx] = 0
        tmp_fishes[0] = (ny, nx, fishes[mat[ny][nx]][2])
        tmp_fishes[mat[ny][nx]] = None
        tmp_mat[y][x] = -1
        q.append((tmp_mat, tmp_fishes, point + mat[ny][nx]))

print(answer)

# print(fishes)
# for i in mat:
#     print(i)