from collections import deque
import sys

input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def check(y, x):
    global wolves, lambs

    queue = deque()
    queue.append((y, x))
    wolf, lamb = 0, 0
    if yard[y][x] == 'o':
        lamb += 1
    elif yard[y][x] == 'v':
        wolf += 1
    yard[y][x] = '#'

    while queue:
        pnt = queue.popleft()
        y, x = pnt[0], pnt[1]

        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]

            if not (ny in range(R) and nx in range(C)) or yard[ny][nx] =='#':
                continue

            if yard[ny][nx] == 'o':
                lamb += 1
            elif yard[ny][nx] == 'v':
                wolf += 1
            yard[ny][nx] = '#'
            queue.append((ny, nx))

    if lamb > wolf:
        lambs += lamb
    else:
        wolves += wolf




R, C = map(int, input().split())
yard = [list(input().rstrip('\n')) for _ in range(R)]
wolves, lambs = 0, 0

for y in range(R):
    for x in range(C):
        if yard[y][x] in 'vo':
            check(y, x)

print(lambs, wolves)