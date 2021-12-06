from collections import deque

dY = (1, 0, -1, 0)
dX = (0, 1, 0, -1)

def bfs(sy, sx, mat):
    q = deque([(sy, sx)])
    mat[sy][sx] = 0
    count = 1

    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dY[d], x + dX[d]
            if ny in range(N) and nx in range(N) and mat[ny][nx]:
                mat[ny][nx] = 0
                count += 1
                q.append((ny, nx))
    return count


N = int(input())
mat = [list(map(int, input())) for _ in range(N)]
complex_cnt = 0
house_cnts = []
for i in range(N):
    for j in range(N):
        if mat[i][j]:
            complex_cnt += 1
            house_cnts.append(bfs(i, j, mat))

print(complex_cnt)
house_cnts.sort()
for c in house_cnts:
    print(c)
