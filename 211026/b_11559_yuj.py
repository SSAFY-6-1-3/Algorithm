import sys
sys.stdin=open('input.txt')
from collections import deque
# 터뜨리고 배열 정리
def move(puyo):
    for col in range(6):
        idx = 11
        for row in range(11, -1, -1):
            if puyo[row][col] == '.':
                continue
            puyo[idx][col], puyo[row][col] = puyo[row][col], puyo[idx][col]
            idx -= 1

# 연속된 색깔 찾기
def bfs(x, y, col):
    check = deque([(x, y)])
    visited = [(x, y)]
    cnt = 1

    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]

    while check:
        x, y = check.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (nx, ny) not in visited:
                if nx in range(12) and ny in range(6) and puyo[nx][ny] == col:
                    cnt += 1
                    visited.append((nx, ny))
                    check.append((nx, ny))

    if cnt >= 4:
        for (i, j) in visited:
            puyo[i][j] = '.'
        return 1
    return 0


puyo = [list(input()) for _ in range(12)]
color = ['R', 'G', 'B', 'P', 'Y']
result = 0

while True:
    bomb = 0
    for x in range(12):
        for y in range(6):
            if puyo[x][y] in color:
                if bfs(x, y, puyo[x][y]):
                    bomb += 1

    if bomb:
        result += 1
    else:
        break

    move(puyo)

print(result)