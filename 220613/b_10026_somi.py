direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(r, c):
    q = [(r, c)]
    visited[r][c] = True
    color = img[r][c]
    while q:
        now_r, now_c = q.pop(0)
        for d in direction:
            next_r = now_r + d[0]
            next_c = now_c + d[1]
            if 0 <= next_r < N and 0 <= next_c < N:
                if img[next_r][next_c] == color:
                    if not visited[next_r][next_c]:
                        q.append((next_r, next_c))
                        visited[next_r][next_c] = True


N = int(input())
img = list(list(input()) for _ in range(N))
visited = list(list(False for _ in range(N)) for _ in range(N))

rgb = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            rgb += 1


for i in range(N):
    for j in range(N):
        visited[i][j] = False
        if img[i][j] == 'G':
            img[i][j] = 'R'

rb = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            rb += 1
print(rgb, rb)
