from collections import deque
import sys

sys.stdin = open('s_1249.txt')

Dy = (1, 0, -1, 0)
Dx = (0, 1, 0, -1)

def check(mat):
    q = deque([(0, 0)])
    dist = [[9999999]*N for _ in range(N)]
    dist[0][0] = 0
    while q:
        y, x = q.popleft()
        now = dist[y][x]
        for d in range(4):
            ny, nx = y+Dy[d], x+Dx[d]
            if ny in range(N) and nx in range(N):
                next = dist[ny][nx]
                if next > now + mat[ny][nx]:
                    dist[ny][nx] = now + mat[ny][nx]
                    q.append((ny, nx))

    return dist[N-1][N-1]





T= int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    print('#{} {}'.format(tc, check(matrix)))