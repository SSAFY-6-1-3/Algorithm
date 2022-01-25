from collections import deque
import sys
input = sys.stdin.readline


dY = (1, 0, -1, 0)
dX = (0, 1, 0, -1)


def bfs(N, M, mat):
    if N*M ==1: return 1

    q = deque([(0, 0, 0)])
    dists = [[[N*M, N*M] for _ in range(M)]for _ in range(N)]
    dists[0][0][0], dists[0][0][1] = 1, 1

    while q:
        y, x, used = q.popleft()
        dist = dists[y][x][used]

        for d in range(4):
            ny, nx = y+dY[d], x+dX[d]
            if ny not in range(N) or nx not in range(M) : continue
            if mat[ny][nx]:
                if used: continue
                if dists[ny][nx][1] <= dist+1: continue
                dists[ny][nx][1] = dist+1
                q.append((ny, nx, 1))
            else:
                if dists[ny][nx][used] <= dist+1: continue
                dists[ny][nx][used] = dist+1
                q.append((ny, nx, used))

    result = min(dists[N-1][M-1])
    if result == N*M:
        return -1
    return result





N, M = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(N)]

print(bfs(N, M, mat))