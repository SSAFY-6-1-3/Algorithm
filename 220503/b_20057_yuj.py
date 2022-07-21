def move(x, y, dx, dy):
    global ans
    if dx == 0:
        direction = [(5, 0, dy*2), (10, -1, dy), (10, 1, dy), (7, -1, 0), (7, 1, 0), (2, -2, 0), (2, 2, 0), (1, -1, -(dy)), (1, 1, -(dy))]
    else:
        direction = [(5, dx*2, 0), (10, dx, -1), (10, dx, 1), (7, 0, -1), (7, 0, 1), (2, 0, -2), (2, 0, 2),
                   (1, -(dx), -1), (1, -(dx), 1)]

    a = matrix[x][y]
    for percent, di, dj in direction:
        nx, ny = x+di, y+dj
        num = int(matrix[x][y] * percent / 100)
        if nx in range(N) and ny in range(N):
            matrix[nx][ny] += num
        else:
            ans += num
        a -= num

    if x+dx in range(N) and y+dy in range(N):
        matrix[x+dx][y+dy] += a
    else:
        ans += a

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
ans = 0
r, c = N//2, N//2
dr = [0,1,0,-1]
dc = [-1,0,1,0]
cnt, d = 1, 0
while True:
    if r == 0 and c == 0:
        break
    if cnt == N-1:
        k = 3
    else:
        k = 2

    for _ in range(k):
        for _ in range(cnt):
            r, c = r+dr[d % 4], c+dc[d % 4]
            move(r, c, dr[d % 4], dc[d % 4])
        d += 1
    cnt += 1

print(ans)