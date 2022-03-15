from collections import deque

N = int(input())
googoo = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    googoo[a][b] = c
    googoo[b][a] = c

dist = [0] * (N+1)
deq = deque([[1, 0]])
while deq:
    x, d = deq.popleft()

    for y in range(2, N+1):
        if googoo[x][y]:
            dist[y] = d+googoo[x][y]
            deq.append([y, d+googoo[x][y]])
            googoo[x][y] = 0
            googoo[y][x] = 0

print(max(dist))