import sys

input = sys.stdin.readline

def inp():
    return map(int, input().split())

class fire:
    def __init__(self, m, s, d):
        self.m = m
        self.s = s
        self.d = d

    def __repr__(self):
        return f"{self.m} {self.s} {self.d}"


def move(y, x, fire):
    dY = (-1, -1, 0, 1, 1, 1, 0, -1)
    dX = (0, 1, 1, 1, 0, -1, -1, -1)
    d = fire.d
    y = (y + dY[d] * fire.s + N) % N
    x = (x + dX[d] * fire.s + N) % N
    return y, x


N, M, K = inp()
mat = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = inp()
    mat[r-1][c-1].append(fire(m, s, d))


def move_all():
    for y in range(N):
        for x in range(N):
            for f in mat[y][x]:
                ny, nx = move(y, x, f)
                fire_tmp.append((f, ny, nx))
            mat[y][x] = []


def combine(fires):
    m, s, d = 0, 0, fires[0].d % 2
    d_same = True
    for f in fires:
        m += f.m
        s += f.s
        if f.d % 2 != d:
            d_same = False

    m //= 5
    s //= len(fires)
    ds = (0, 2, 4, 6) if d_same else (1, 3, 5, 7)

    if not m:
        return []
    tmp = []
    for d in ds:
        tmp.append(fire(m, s, d))
    return tmp


def spread(fire_tmp):
    for f, y, x in fire_tmp:
        mat[y][x].append(f)


def combine_all():
    for y in range(N):
        for x in range(N):
            if len(mat[y][x]) > 1:
                mat[y][x] = combine(mat[y][x])


for _ in range(K):
    fire_tmp = []
    move_all()
    spread(fire_tmp)
    combine_all()

answer = 0
for y in range(N):
    for x in range(N):
        for f in mat[y][x]:
            answer += f.m

print(answer)