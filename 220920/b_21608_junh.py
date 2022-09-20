import sys

input = sys.stdin.readline
dY = (0, 1, 0, -1)
dX = (1, 0, -1, 0)

N = int(input())

mat = [[0]*N for _ in range(N)]
ngbs = [[set() for _ in range(N)] for _ in range(N)]

def value(y, x, like):
    pnt = 0
    bns = 0
    for d in range(4):
        ny, nx = y + dY[d], x + dX[d]

        if ny not in range(N) or nx not in range(N): continue

        if mat[ny][nx] in like:
            if pnt < 1:
                pnt = 1
            else:
                pnt *= 10
        elif not mat[ny][nx]:
            bns += 0.1

    return pnt + bns


def solve(num, like):
    target = (0, 0, -1) # y, x, pnt

    for y in range(N):
        for x in range(N):
            if mat[y][x]: continue
            v = value(y, x, like)
            if v > target[2]:
                target = (y, x, v)
    y, x, v = target
    mat[y][x] = num


likes = {}
for _ in range(N**2):
    inp = list(map(int, input().split()))
    n, like = inp[0], inp[1:]
    likes[n] = like
    solve(n, like)

answer = 0
for y in range(N):
    for x in range(N):
        answer += int(value(y, x, likes[mat[y][x]]))

print(answer)