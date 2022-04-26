from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
deq = deque([[0, 0, 1]])
miro[0][0] = 0

while deq:
    x, y, cnt = deq.popleft()
    if x == N-1 and y == M-1:
        print(cnt)
        break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx in range(N) and ny in range(M) and miro[nx][ny]:
            deq.append([nx, ny, cnt+1])
            miro[nx][ny] = 0
