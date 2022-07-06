
N = int(input())

if N == 1:
    print('*')
    exit()

dY = (-1, 0, 1, 0)
dX = (0, 1, 0, -1)
garo, sero = (N-1)*4 + 1, (N-1)*4 + 3
mat = [[' ' for  _ in range(garo)] for _ in range(sero)]

y, x = sero//2 + 1, garo//2
mat[y][x] = '*'
d = 0
length = 3
cnt = 0
start = True
while not (y == 0 and x == garo):
    mat[y][x] = '*'
    cnt += 1
    if cnt == length:
        if d % 2:
            length += 2
        if start:
            if d % 2:
                length = 4
                start = False
            else:
                length = 2
        d = (d+1)%4
        cnt = 0

    y, x = y + dY[d], x + dX[d]



for i in mat:
    print(''.join(i).strip())

# 2 - 7(3+4)
# 3 - 11(3+8)
# 4 - 15(3+12)