import sys

def inp():
    return map(int, input().split())

input = sys.stdin.readline
D = [None, (-1, 0), (1, 0), (0, -1), (0, 1)]

class Shark:
    cnt = 0
    def __init__(self, num = 0, y = -1, x = -1):
        self.alive = True
        self.num = num
        self.y = y
        self.x = x
        if self.num == 0:
            self.alive = False
        else:
            Shark.cnt += 1

    def set_dir(self, d):
        self.dir = d

    def set_pref(self):
        self.pref = [[]] + [list(inp()) for _ in range(4)]

    def move(self, d):
        ny, nx = self.new_point(d)
        self.dir = d
        self.y, self.x = ny, nx

    def kill(self):
        self.alive = False
        Shark.cnt -= 1

    def new_point(self, d):
        return self.y + D[d][0], self.x + D[d][1]

    def try_move(self):
        pref = self.pref[self.dir]

        for d in pref:
            ny, nx = self.new_point(d)
            if ny not in range(N) or nx not in range(N):
                continue
            if mat[ny][nx][0] == 0:
                self.move(d)
                return

        for d in pref:
            ny, nx = self.new_point(d)
            if ny not in range(N) or nx not in range(N):
                continue
            if mat[ny][nx][0] == self.num:
                self.move(d)
                return

    def try_smell(self):
        winner = self.num
        if mat[self.y][self.x][1] == k:
            live, dead = sorted([self.num, mat[self.y][self.x][0]])
            sharks[dead].kill()
            winner = sharks[live].num
        sharks[winner].smell()

    def smell(self):
        mat[self.y][self.x] = [self.num, k]


N, M, k = inp()
sharks: [Shark] = [Shark()] * (M+1)
mat = []    # (num, last)

for i in range(N):
    mat.append([])
    line = list(inp())
    for j in range(N):
        s = line[j]
        if s:
            sharks[s] = Shark(s, i, j)
        mat[i].append([s, k * (s != 0)])

dirs = [None] + list(inp())
for i in range(1, M+1):
    sharks[i].set_dir(dirs[i])
    sharks[i].set_pref()


def solve():
    sec = 0

    while sec <= 1000 and Shark.cnt > 1:
        sec += 1

        for i in range(1, M+1):
            sh = sharks[i]
            if sh.alive:
                sh.try_move()

        for i in range(N):
            for j in range(N):
                if mat[i][j][0]:
                    mat[i][j][1] -= 1
                    if not mat[i][j][1]:
                        mat[i][j][0] = 0

        for i in range(1, M+1):
            sh = sharks[i]
            if sh.alive:
                sh.try_smell()

    if sec > 1000:
        return -1
    return sec


print(solve())


