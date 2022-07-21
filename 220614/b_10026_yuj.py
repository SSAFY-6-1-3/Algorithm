# dfs로 하니까 recursion error
from collections import deque

def move(i, j, color, visited):
    que = deque([[i, j]])
    while que:
        i, j = que.popleft()
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if ni in range(N) and nj in range(N):
                if color == matrix[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    que.append([ni, nj])

def check():
    num = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                move(i, j, matrix[i][j], visited)
                num += 1
    answer.append(num)

N = int(input())
matrix = [list(input()) for _ in range(N)]
answer = []
check()
for x in range(N):
    for y in range(N):
        if matrix[x][y] == 'R':
            matrix[x][y] = 'G'
check()
print(*answer)