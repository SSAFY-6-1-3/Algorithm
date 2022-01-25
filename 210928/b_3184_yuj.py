import sys
sys.stdin=open('input.txt')

def bfs(x, y):
    global w, s, visited
    check = [[x,y]]
    while check:
        x, y = check.pop()

        visited[x][y] = 1

        if ground[x][y] == 'v':
            w += 1

        elif ground[x][y] == 'o':
            s += 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < R and 0 <= ny < C and ground[nx][ny] != '#' and not visited[nx][ny]:
                check.append([nx, ny])



R, C = map(int, input().split())

ground = []
for _ in range(R):
    ground.append(list(input()))

visited = [[0] * C for _ in range(R)]           # 방문 체크
     # 좌 우 상 하
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]


wolf = 0
sheep = 0
for x in range(R):
    for y in range(C):
        if not visited[x][y] and ground[x][y] != '#':
            w, s = 0, 0
            bfs(x, y)
            if w >= s:
                wolf += w
            elif w < s:
                sheep += s

print(sheep, wolf)