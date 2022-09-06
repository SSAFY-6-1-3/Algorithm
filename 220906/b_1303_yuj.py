def bfs(x, y):
    global dx, dy, cnt, color

    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if nx in range(M) and ny in range(N) and soldiers[nx][ny]:
            if soldiers[nx][ny] == color:
                soldiers[nx][ny] = 0
                cnt += 1
                bfs(nx, ny)


N, M = map(int, input().split())
soldiers = [list(map(str, input())) for _ in range(M)]
white, blue = 0, 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(M):
    for j in range(N):
        cnt = 1
        if soldiers[i][j]:
            color = soldiers[i][j]
            soldiers[i][j] = 0
            bfs(i, j)
            if color == 'W':
                white += cnt ** 2
            else:
                blue += cnt ** 2
print(white, blue)