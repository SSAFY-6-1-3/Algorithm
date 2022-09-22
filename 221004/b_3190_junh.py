from collections import deque

dY = (0, 1, 0, -1)
dX = (1, 0, -1, 0)

N = int(input())
K = int(input())
mat = [[0] * N for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    mat[y-1][x-1] = 1
L = int(input())
moves = []
for _ in range(L):
    x, c = input().split()
    moves.append((int(x), c))


def play(moves):
    snake = deque([(0, 0)])
    mat[0][0] = -1
    d = 0
    m_idx = 0
    sec = 0
    while True:
        sec += 1
        y, x = snake[-1]

        ny, nx = y + dY[d], x + dX[d]

        if ny not in range(N) or nx not in range(N):
            return sec
        else:
            if mat[ny][nx] == 1:
                mat[ny][nx] = 0
            elif mat[ny][nx] == -1:
                return sec
            else:
                py, px = snake.popleft()
                mat[py][px] = 0
            snake.append((ny, nx))
            mat[ny][nx] = -1

        if m_idx < len(moves) and sec == moves[m_idx][0]:
            if moves[m_idx][1] == 'L':
                d = (d + 3) % 4
            else:
                d = (d + 1) % 4
            m_idx += 1


print(play(moves))