
def Z(n, st_num, sy, sx):
    if sy == r and sx == c:
        return st_num
    size = 2**n

    if r in range(sy, sy+size):
        if c in range(sx, sx+size):
            return Z(n-1, st_num, sy, sx)
        else:
            return Z(n-1, st_num + size**2, sy, sx+size)
    else:
        if c in range(sx, sx+size):
            return Z(n-1, st_num + size**2 * 2, sy+size, sx)
        else:
            return Z(n-1, st_num + size**2 * 3, sy+size, sx+size)

N, r, c = map(int, input().split())
KEY_NUM = 0
print(Z(N-1, 0, 0, 0))




# def Z(n, sy, sx, mat):
#     global KEY_NUM
#     if n == -1:
#         mat[sy][sx] = KEY_NUM
#         KEY_NUM += 1
#         return
#     size = 2**n
#
#     Z(n-1, sy, sx, mat)
#     Z(n-1, sy, sx+size, mat)
#     Z(n-1, sy+size, sx, mat)
#     Z(n-1, sy+size, sx+size, mat)