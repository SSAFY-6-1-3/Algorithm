'''
시간초과
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def tomato(ripe):
    days = -1
    while ripe:
        q = ripe
        ripe = []
        days += 1
        while q:
            r, c = q.pop(0)
            for di in range(4):
                nr, nc = r + dr[di], c + dc[di]
                if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0:
                    box[nr][nc] = 1
                    ripe.append((nr, nc))
    return days

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

ripened = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            ripened.append((i, j))
ans = tomato(ripened)

flag = True
for line in box:
    if 0 in line:
        print(-1)
        flag = False
        break

if flag:
    print(ans)

'''

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def tomato():
    while q:
        r, c = q.popleft()
        for di in range(4):
            nr, nc = r + dr[di], c + dc[di]
            if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0:
                box[nr][nc] = box[r][c] + 1
                q.append((nr, nc))

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))
tomato()

flag = True
ans = 0
for line in box:
    ans = max(ans, max(line))
    if 0 in line:
        print(-1)
        flag = False
        break

if flag:
    print(ans - 1)
