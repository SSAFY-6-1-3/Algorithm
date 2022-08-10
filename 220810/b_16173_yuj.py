def jump(x, y):
    global flag

    if x == N-1 and y == N-1:
        flag = 1
        return

    cnt = jelly[x][y]
    jelly[x][y] = 0
    for k in range(2):
        nx, ny = x + cnt * dx[k], y + cnt * dy[k]
        if nx in range(N) and ny in range(N) and jelly[nx][ny]:
            jump(nx, ny)

N = int(input())
jelly = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0]
dy = [0, 1]
flag = 0
jump(0, 0)
if flag:
    print('HaruHaru')
else:
    print('Hing')