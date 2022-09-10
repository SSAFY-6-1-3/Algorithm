
N, M = map(int, input().split())
r, c, d = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

class Vacuum:
    dY = (-1, 0, 1, 0)
    dX = (0, -1, 0, 1)

    def __init__(self, y, x, d):
        self.y = y
        self.x = x
        self.dir = d
        self.cleaned = 0

    def clean(self):
        if not mat[self.y][self.x] :
            mat[self.y][self.x] = 2
            self.cleaned += 1

    def move(self, pnts):
        self.y = pnts[0]
        self.x = pnts[1]

    def check(self, to_clean):
        ny = self.y + Vacuum.dY[self.dir]
        nx = self.x + Vacuum.dX[self.dir]

        if ny not in range(N) or nx not in range(M):
            return False
        if mat[ny][nx] == 1 or (to_clean and mat[ny][nx] == 2) :
            return False
        return ny, nx

    def func12(self):
        for _ in range(4):
            self.dir = (self.dir + 1) % 4
            chk = self.check(True)
            if chk:
                self.move(chk)
                return True
        return False

    def back(self):
        self.dir = (self.dir + 2) % 4
        chk = self.check(False)
        self.dir = (self.dir + 2) % 4
        if chk:
            self.move(chk)
            return True
        else:
            return False


vac = Vacuum(r, c, d)
while True:
    vac.clean()
    print(vac.y, vac.x)
    if vac.func12():
        continue
    if vac.back():
        continue
    break

print(vac.cleaned)
for l in mat:
    print(l)