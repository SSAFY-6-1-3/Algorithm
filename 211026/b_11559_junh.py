Dy = (1, 0, -1, 0)
Dx = (0, 1, 0, -1)

def down(mat):
    for i in range(6):
        temp = []
        for j in range(12):
            if mat[j][i] != '.':
                temp.append(mat[j][i])
        for j in range(11, -1, -1):
            if temp:
                mat[j][i] = temp.pop()
            else:
                mat[j][i] = '.'


def bfs(sy, sx):
    col = mat[sy][sx]
    q = [(sy, sx)]
    head = 0

    while head < len(q):
        y, x = q[head]
        head += 1

        for d in range(4):
            ny, nx = y+Dy[d], x+Dx[d]
            if ny not in range(12) or nx not in range(6): continue
            if (ny, nx) in q or mat[ny][nx] != col: continue
            q.append((ny, nx))

    if len(q)>=4:
        for pnt in q:
            y, x = pnt
            mat[y][x] = '.'
        return True
    else:
        return False




def puyo(mat):
    cnt = 0
    chain = True
    while chain:
        chain = False

        for y in range(12):
            for x in range(6):
                if mat[y][x] != '.':
                    if bfs(y, x):
                        chain = True
        if chain:
            cnt +=1
            down(mat)
    return cnt



mat = [list(input()) for _ in range(12)]
print(puyo(mat))