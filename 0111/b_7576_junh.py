from collections import deque

dY = (1, 0, -1, 0)
dX = (0, 1, 0, -1)

def has_zero(box, M, N):
    for i in range(N):
        for j in range(M):
            if not box[i][j]:
                return True
    return False

def bfs(q, M, N, box):
    q = deque(q)

    while q:
        y, x = q.popleft()
        dist = box[y][x]
        for d in range(4):
            ny, nx = y+dY[d], x+dX[d]
            if ny not in range(N) or nx not in range(M): continue
            if box[ny][nx] and box[ny][nx] <= dist+1: continue

            box[ny][nx] = dist + 1
            q.append((ny, nx))

    if has_zero(box, M, N):
        return -1
    return max(map(max, box)) - 1


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
q = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))

print(bfs(q, M, N, box))