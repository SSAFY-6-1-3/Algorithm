from collections import deque


def bfs(starts):
    global max_day
    q = deque(starts)

    while q:
        h, n, m = q.popleft()
        day = visited[h][n][m]

        for dH, dN, dM in dYXH:
            nH, nN, nM = h + dH, n + dN, m + dM

            if nH not in range(H) or nN not in range(N) or nM not in range(M) or tomatoes[nH][nN][nM] == -1:
                continue
            if day + 1 < visited[nH][nN][nM] or visited[nH][nN][nM] == -1:
                visited[nH][nN][nM] = day + 1
                max_day = max(max_day, day + 1)
                q.append((nH, nN, nM))


def get_answer():
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if visited[h][n][m] == -1:
                    return -1
    return 0


M, N, H = map(int, input().split())

tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dYXH = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1))

starts = []
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 1:
                starts.append((h, n, m))
            elif tomatoes[h][n][m] == 0:
                visited[h][n][m] = -1
            else:
                visited[h][n][m] = -2


max_day = 0
bfs(starts)
if get_answer():
    max_day = -1
print(max_day)