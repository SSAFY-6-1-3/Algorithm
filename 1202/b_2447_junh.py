N = int(input())
mat = [[' ' for _ in range(N)] for _ in range(N)]

def draw(y, x, size):
    if size==1:
        mat[y][x] = '*'
        return
    b_size = size//3

    draw(y, x, b_size)
    draw(y+b_size, x, b_size)
    draw(y+2*b_size, x, b_size)

    draw(y, x+b_size, b_size)
    draw(y + 2 * b_size, x+b_size, b_size)

    draw(y, x+2*b_size, b_size)
    draw(y+b_size, x+2*b_size, b_size)
    draw(y+2*b_size, x+2*b_size, b_size)

def prt(mat):
    for i in range(N):
        print(''.join(mat[i]))

draw(0, 0, N)
prt(mat)


