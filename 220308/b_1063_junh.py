import sys
input = sys.stdin.readline


drc = {
    'R' : (0, 1),
    'L' : (0, -1),
    'B' : (1, 0),
    'T' : (-1, 0)
}

def st_p(st):
    y = 8 - int(st[1])
    x = ord(st[0]) - ord('A')
    return [y, x]

def p_st(p):
    a = chr(ord('A') + p[1])
    b = str(8-p[0])
    return a+b

def command(st):
    mY, mX = 0, 0
    for comm in st:
        mY += drc[comm][0]
        mX += drc[comm][1]
    return mY, mX

def move(ml, c, is_king):
    global D
    ny, nx = ml[0]+c[0], ml[1]+c[1]
    if ny not in range(8) or nx not in range(8):
        return ml

    if is_king and ny==D[0] and nx==D[1]:
        D = move(D, c, False)
        if ny==D[0] and nx==D[1]:
            return ml

    return [ny, nx]



K, D, N = input().split()
N = int(N)
K, D = st_p(K), st_p(D)

for _ in range(N):
    c = command(input().strip())
    K = move(K, c, True)
print(p_st(K), p_st(D), sep='\n')
