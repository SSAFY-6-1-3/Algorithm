from collections import deque

mat = [input().split() for _ in range(5)]
dY = (0, 1, 0, -1)
dX = (1, 0, -1, 0)
combs = set()

def dfs(y, x, result):
    if len(result) == 6:
        combs.add(result)
        return

    for d in range(4):
        ny, nx = y + dY[d], x + dX[d]

        if ny in range(5) and nx in range(5):
            dfs(ny, nx, result + mat[ny][nx])


for i in range(5):
    for j in range(5):
        dfs(i, j, mat[i][j])


print(len(combs))

