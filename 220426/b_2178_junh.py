from collections import deque

N, M = map(int, input().split())
mat = [list(map(int, input())) for _ in range(N)]

def bfs(mat, N, M):
    dY = (1, 0, -1, 0)
    dX = (0, 1, 0, -1)
    counts = [[0]*M for _ in range(N)]
    q = deque([(0, 0)])
    mat[0][0], counts[0][0] = 0, 1
    while q:
        y, x = q.popleft()
        dist = counts[y][x]

        for d in range(4):
            ny, nx = y+dY[d], x+dX[d]
            if ny not in range(N) or nx not in range(M) or not mat[ny][nx]: continue
            if ny == N-1 and nx == M-1: return dist+1
            mat[ny][nx] = 0
            counts[ny][nx] = dist+1
            q.append((ny, nx))

print(bfs(mat, N, M))