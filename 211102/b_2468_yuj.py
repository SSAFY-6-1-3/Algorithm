import sys
sys.stdin=open('input.txt')
from collections import deque

def bfs(i, j):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque([(i, j)])

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if arr[nx][ny] > h and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1


N = int(input())
arr = [[-1] * (N+2)] +[[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (N+2)]
maxv, area = 1, 1

while area > 0:
    for h in range(101):
        area = 0
        visited = [[0] *(N+2) for _ in range(N+2)]
        for x in range(1, N+1):
            for y in range(1, N+1):
                if arr[x][y] > h and not visited[x][y]:
                    visited[x][y] = 1
                    bfs(x, y)
                    area += 1
        if maxv < area:
            maxv = area

print(maxv)
