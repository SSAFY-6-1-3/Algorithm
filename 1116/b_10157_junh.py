dX = (0, 1, 0, -1)
dY = (1, 0, -1, 0)

def find(target):
    y, x = -1, 0
    d = 0
    for i in range(1, c*r+1):
        ny, nx = y+dY[d], x+dX[d]
        if ny not in range(r) or nx not in range(c) or mat[ny][nx]:
            d = (d+1)%4
            ny, nx = y+dY[d], x+dX[d]
        mat[ny][nx] = i
        if i == target:
            print(nx+1, ny+1)
            return
        y, x = ny, nx
    print(0)


c, r = map(int, input().split())
t = int(input())
mat = [[0 for _ in range(c)] for _ in range(r)]

find(t)


