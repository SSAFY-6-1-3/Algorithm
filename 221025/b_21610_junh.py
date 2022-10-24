
N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

dY = (0, -1, -1, -1, 0, 1, 1, 1)
dX = (-1, -1, 0, 1, 1, 1, 0, -1)

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1

    for i in range(len(clouds)):
        y, x = clouds[i]
        y = (y + dY[d]*s) % N
        x = (x + dX[d]*s) % N
        clouds[i] = (y, x)
        mat[y][x] += 1

    for cloud in clouds:
        y, x = cloud
        cnt = 0
        for dg in range(1, 8, 2):
            ny, nx = y + dY[dg], x + dX[dg]
            if 0 <= ny < N and 0 <= nx < N and mat[ny][nx]:
                cnt += 1
        mat[y][x] += cnt

    new_clouds = []

    for y in range(N):
        for x in range(N):
            if mat[y][x] >= 2 and (y, x) not in clouds:
                new_clouds.append((y, x))
                mat[y][x] -= 2
    clouds = new_clouds


answer = 0
for y in range(N):
    for x in range(N):
        answer += mat[y][x]
print(answer)

