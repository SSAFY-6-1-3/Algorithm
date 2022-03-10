chess = [[0] * 8 for _ in range(8)]
king, stone, N = map(str, input().split())
k = [8-int(king[1]), ord(king[0])-65]
s = [8-int(stone[1]), ord(stone[0])-65]
dic = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1),
}

for _ in range(int(N)):
    move = input()
    dx, dy = dic[move]
    nx, ny = k[0] + dx, k[1] + dy
    nsx, nsy = s[0] + dx, s[1] + dy
    if nx in range(8) and ny in range(8):
        if nx == s[0] and ny == s[1]:
            if nsx in range(8) and nsy in range(8):
                k = [nx, ny]
                s = [nsx, nsy]
        else:
            k = [nx, ny]

rk = ''.join([chr(k[1]+65), str(8-k[0])])
rs = ''.join([chr(s[1]+65), str(8-s[0])])
print(rk)
print(rs)