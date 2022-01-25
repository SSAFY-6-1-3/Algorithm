from collections import deque

def solution(maps):
    answer = 0
    dY = (1, 0, -1, 0)
    dX = (0, 1, 0, -1)

    n = len(maps)
    m = len(maps[0])
    dists = [[0 for _ in range(m)] for _ in range(n)]

    q = deque([(0, 0)])
    dists[0][0] = 1

    while q and not dists[n-1][m-1]:
        y, x = q.popleft()
        dist = dists[y][x]

        for d in range(4):
            ny, nx = y+dY[d], x+dX[d]

            if ny not in range(n) or nx not in range(m) or maps[ny][nx]==0: continue
            if dists[ny][nx] > dist+1 or not dists[ny][nx]:
                dists[ny][nx] = dist +1
                q.append((ny, nx))
    if dists[n-1][m-1]:
        return dists[n-1][m-1]
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))