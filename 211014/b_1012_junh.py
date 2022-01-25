import sys
from collections import deque

input = sys.stdin.readline


Dx = (1, 0, -1, 0)
Dy = (0, 1, 0, -1)

def check(farm):
    answer = 0

    for i in range(N):
        for j in range(M):
            if farm[i][j]:
                answer +=1
                bfs(i, j)
    return answer

def bfs(i, j):
    q = deque([(i, j)])
    farm[i][j] = 0

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny, nx = y+Dy[d], x+Dx[d]
            if ny not in range(N) or nx not in range(M) or not farm[ny][nx]:
                continue
            q.append((ny, nx))
            farm[ny][nx] = 0


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    print(check(farm))