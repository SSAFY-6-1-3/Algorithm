import sys
sys.stdin=open('input.txt')
from collections import deque

# pypy에서 통과
def bfs(si, sj, cnt):

    di = [0, 0, -1, +1]
    dj = [-1, +1, 0, 0]
    queue = deque([(si, sj, cnt)])

    while queue:
        i, j, cnt = queue.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if ni in range(r) and nj in range(c):
                if check[ni][nj] == 'L':
                    if dist[ni][nj] < cnt+1:
                        dist[ni][nj] = cnt+1
                    check[ni][nj] = 'W'
                    queue.append((ni, nj, cnt+1))


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
dist = [[0 for _ in range(c)] for _ in range(r)]

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'L':
            check = [item[:] for item in arr]
            check[i][j] = 'W'
            bfs(i, j, 0)

print(max(map(max, dist)))
