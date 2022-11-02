import sys
from collections import deque

input = sys.stdin.readline
N, Q = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(2**N)]
ls = list(map(int, input().split()))
dY = (0, 1, 0, -1)
dX = (1, 0, -1, 0)


def rotate(size):
    for sy in range(0, 2**N, size):
        for sx in range(0, 2**N, size):
            tmp = [[0]*size for _ in range(size)]
            for i in range(size):
                y = sy + i
                for j in range(size):
                    x = sx + j
                    tmp[j][size-1-i] = mat[y][x]
            for i in range(size):
                y = sy + i
                for j in range(size):
                    x = sx + j
                    mat[y][x] = tmp[i][j]


def minus_check(y, x):
    cnt = 0
    for d in range(4):
        ny, nx = y + dY[d], x + dX[d]
        if ny not in range(2**N) or nx not in range(2**N) or not mat[ny][nx]:
            continue
        cnt += 1

    if cnt < 3:
        return False
    return True


def bfs(y, x):
    global ice_sum
    q = deque([(y, x)])
    visited[y][x] = True
    ice_sum += mat[y][x]
    ice = 1

    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y+ dY[d], x + dX[d]
            if ny not in range(2**N) or nx not in range(2**N) or not mat[ny][nx] or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            ice_sum += mat[ny][nx]
            ice += 1
            q.append((ny, nx))
    return ice


for l in ls:
    size = 2 ** l
    rotate(size)

    minus = []
    for i in range(2**N):
        for j in range(2**N):
            if mat[i][j] > 0 and not minus_check(i, j):
                minus.append((i, j))
    for y, x in minus:
        mat[y][x] -= 1



visited = [[0] * 2**N for _ in range(2**N)]
ice_sum = 0
max_ice = 0
for i in range(2**N):
    for j in range(2**N):
        if mat[i][j] and not visited[i][j]:
            max_ice = max(max_ice, bfs(i, j))

print(ice_sum)
print(max_ice)

