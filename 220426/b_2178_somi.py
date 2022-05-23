dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    minCnt = N * M
    q = [(0, 0, 1)]
    while q:
        r, c, step = q.pop(0)

        if r == N - 1 and c == M - 1:
            minCnt = min(minCnt, step)

        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]

            if 0 <= next_r < N and 0 <= next_c < M and maze[next_r][next_c]:
                q.append((next_r, next_c, step + 1))
                maze[next_r][next_c] = 0

    return minCnt


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

print(bfs())