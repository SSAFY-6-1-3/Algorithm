# PyPy3 통과
# python 시간초과

import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def treasure(i, j):
    checked = list([False] * C for _ in range(R))
    dist = 0
    q = [(i, j, 0)]
    checked[i][j] = True
    while q:
        r, c, cnt = q.pop(0)

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and not checked[nr][nc] and map[nr][nc] == 'L':
                checked[nr][nc] = True
                q.append((nr, nc, cnt + 1))
                if cnt + 1 > dist:
                    dist = cnt + 1


    return dist



R, C = map(int, input().split())
map = list(input() for _ in range(R))
max_dist = 0
for i in range(R):
    for j in range(C):
        if map[i][j] == 'L':
            tmp = treasure(i, j)

            if tmp > max_dist:
                max_dist = tmp


print(max_dist)