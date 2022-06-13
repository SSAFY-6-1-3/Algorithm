from collections import deque

dY = (1, 0, -1, 0)
dX = (0, 1, 0, -1)

def bfs(pnt, sy, sx, visited, SY):
    q = deque([(sy, sx)])
    visited[sy][sx] = True

    while q:
        y, x = q.popleft()
        col = pnt[y][x]
        for d in range(4):
            ny, nx = y + dY[d], x + dX[d]
            if ny not in range(N) or nx not in range(N) or visited[ny][nx]:
                continue
            n_col = pnt[ny][nx]

            if not SY and col != n_col : continue
            elif SY and col != n_col and (col == 'B' or n_col == 'B') : continue

            q.append((ny, nx))
            visited[ny][nx] = True


N = int(input())
pnt = [input() for _ in range(N)]

asy_visited = [[False for _ in range(N)] for _ in range(N)]
sy_visited = [[False for _ in range(N)] for _ in range(N)]
asy_cnt, sy_cnt = 0, 0

for i in range(N):
    for j in range(N):
        if not asy_visited[i][j]:
            asy_cnt += 1
            bfs(pnt, i, j, asy_visited, False)
        if not sy_visited[i][j]:
            sy_cnt += 1
            bfs(pnt, i, j, sy_visited, True)

print(asy_cnt, sy_cnt)