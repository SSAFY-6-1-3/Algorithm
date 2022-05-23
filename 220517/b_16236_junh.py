from collections import deque


def dist(y, x):
    return abs(sy - y) + abs(sx - x)

def is_smaller(fish):
    if fishes[fish] < size: return True
# # return min(eatables, key=lambda x: (dist(x[0], x[1]), x[0], x[1]))

def bfs(eatables):
    global sy, sx
    q = deque([(sy, sx, 0)])
    visited = {(sy, sx)}

    min_eatables = []
    min_cnt = float('INF')
    while q:
        y, x, cnt = q.popleft()
        if cnt > min_cnt : break
        for d in range(4):
            ny, nx = y + dY[d], x + dX[d]
            if not (ny in range(N) and nx in range(N)) or (ny, nx) in visited: continue

            if not mat[ny][nx] or mat[ny][nx] == size: pass
            elif mat[ny][nx] > size: continue
            else:
                min_cnt = cnt
                min_eatables.append((ny, nx, cnt))
                visited.add((ny, nx))
                continue


            visited.add((ny, nx))
            q.append((ny, nx, cnt+1))

    if not min_eatables:
        return 0
    target = min(min_eatables)
    ty, tx, cnt = target
    fishes.pop((ty, tx))
    mat[ty][tx] = 0
    sy, sx = ty, tx
    return cnt + 1



N = int(input())
dY = (-1, 0, 0, 1)
dX = (0, -1, 1, 0)

mat = [list(map(int, input().split())) for _ in range(N)]
sy, sx = 0,0
fishes = {}
for i in range(N):
    for j in range(N):
        if mat[i][j]:
            if mat[i][j] == 9:
                mat[i][j] = 0
                sy, sx = i, j
            else:
                fishes[(i, j)] = mat[i][j]


size = 2
eat = 0
sec = 0
while fishes:
    eatables = list(filter(is_smaller, fishes))
    if not eatables: break
    result = bfs(eatables)
    if not result:
        break
    eat += 1

    if eat == size:
        size += 1
        eat = 0
    sec += result

print(sec)
