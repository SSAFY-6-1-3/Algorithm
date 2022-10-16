N = int(input())
mat = [[False] * 101 for _ in range(101)]
dY = (0, -1, 0, 1)
dX = (1, 0, -1, 0)

for _ in range(N):
    x, y, d, g = map(int, input().split())
    mat[y][x] = True
    y += dY[d]
    x += dX[d]
    mat[y][x] = True
    stack = [d]

    for _ in range(g):
        for i in range(len(stack)-1, -1, -1):
            d = (stack[i] + 1) % 4
            y += dY[d]
            x += dX[d]
            mat[y][x] = True
            stack.append(d)

cnt = 0
for y in range(100):
    for x in range(100):
        if mat[y][x] and mat[y+1][x] and mat[y][x+1] and mat[y+1][x+1]:
            cnt += 1

print(cnt)
