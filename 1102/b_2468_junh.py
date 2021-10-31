import copy
from collections import deque
import sys

input = sys.stdin.readline

dY = (1, 0, -1, 0)
dX = (0, 1, 0, -1)

def bfs(sy, sx, h, tmp):
    q = deque([(sy, sx)])
    tmp[sy][sx] = 0

    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y+dY[d], x+dX[d]
            if ny not in range(N) or nx not in range(N): continue
            if tmp[ny][nx] > h:
                tmp[ny][nx] = 0
                q.append((ny, nx))



def safe(N, mat):
    max_h = max(map(max, mat))
    max_safe = 1

    for h in range(max_h-1, -1, -1):
        tmp = copy.deepcopy(mat)
        safes = 0
        for y in range(N):
            for x in range(N):
                if tmp[y][x] > h:
                    bfs(y, x, h, tmp)
                    safes+=1
        max_safe = max(max_safe, safes)

    return max_safe

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
print(safe(N, mat))

