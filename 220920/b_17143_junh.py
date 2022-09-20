
R, C, M = map(int, input().split())
dY = (-1, 1, 0, 0)
dX = (0, 0, 1, -1)
mat = [[0]*C for _ in range(R)]
sharks = [None]
for n in range(M):
    r, c, s, d, z = map(int, input().split())
    mat[r-1][c-1] = n + 1
    sharks.append([r-1, c-1, s, d-1, z])


def catch(c):
    for r in range(R):
        n = mat[r][c]
        if n:
            z = sharks[n][4]
            sharks[n] = None
            mat[r][c] = 0
            return z
    return 0

def calc(p, lim):
    lim -= 1
    is_l = (p < 0)
    p = abs(p)

    d = (((p-1) // lim + 1) % 2)
    p = (p-1) % lim + 1

    if is_l != d :
        return p, is_l != d
    else:
        return lim - 1 - p, is_l != d


def move():
    global sharks

    for i in range(1, len(sharks)):
        if not sharks[i]: continue
        r, c, s, d, z = sharks[i]
        mat[r][c] = 0
        ny, nx = r + dY[d] * s, c + dX[d] * s
        chg = False

        if ny not in range(R):
            ny, chg = calc(ny, R)
        elif nx not in range(C):
            nx, chg = calc(nx, C)
        if chg:
            d = d//2*2 + (d+1)%2
        sharks[i] = [ny, nx, s, d, z]

    for i in range(1, len(sharks)):
        if not sharks[i]: continue
        r, c, s, d, z = sharks[i]
        n = mat[r][c]
        if n and sharks[n][4] > z:
            sharks[i] = None
            continue
        mat[r][c] = i


caught = 0
for c in range(C):
    caught += catch(c)
    move()
print(caught)