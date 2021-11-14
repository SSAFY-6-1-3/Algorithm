from collections import deque
import sys

input = sys.stdin.readline

dY = (1, 0, -1, 0)
dX = (0, 1, 0, -1)

def bfs(sy, sx):
    q = deque([(sy, sx)])
    checked[sy][sx] = 0
    s_pnts = []
    while q:
        y, x = q.popleft()
        dist = checked[y][x]
        cnt = 0
        for d in range(4):
            ny, nx = y+dY[d], x+dX[d]
            if ny not in range(r) or nx not in range(c):
                cnt +=1
                continue
            if mat[ny][nx]=='W' or checked[ny][nx] != -3:
                cnt +=1
                continue

            checked[ny][nx] = dist+1
            q.append((ny, nx))
        if cnt == 4:
            s_pnts.append((y, x))
    return s_pnts, max(map(max, checked))

r, c = map(int, input().strip().split())
mat = [input() for _ in range(r)]
checked = [[-3 for _ in range(c)] for _ in range(r)]
start_points=[]
for sy in range(r):
    for sx in range(c):
        if mat[sy][sx]=='L' and checked[sy][sx]==-3:
            start_points.extend(bfs(sy, sx)[0])

max_dist = 0
for sp in start_points:
    checked = [[-3 for _ in range(c)] for _ in range(r)]
    sy, sx = sp
    max_dist = max(max_dist, bfs(sy, sx)[1])
print(max_dist)