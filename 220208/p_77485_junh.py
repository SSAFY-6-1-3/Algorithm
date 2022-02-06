dY = (0, 1, 0, -1)
dX = (1, 0, -1, 0)

def solution(rows, columns, queries):
    answer = []
    mat= [[(columns*j)+i+1 for i in range(columns)] for j in range(rows)]

    for query in queries:
        sy, sx, ey, ex = query
        sy, sx, ey, ex = sy-1, sx-1, ey-1, ex-1

        y, x, d = sy, sx, 0
        cnt, new = 0, mat[y][x]
        min_n = mat[ey][ex]
        while d < 4:
            if y+dY[d] in range(sy, ey+1) and x+dX[d] in range(sx, ex+1):
                old = new
                y, x = y+dY[d], x+dX[d]
                new = mat[y][x]
                min_n = min(min_n, new)
                mat[y][x] = old
                cnt += 1
            else:
                d +=1
        answer.append(min_n)

    return answer



print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(100, 97, [[1,1,100,97]]))