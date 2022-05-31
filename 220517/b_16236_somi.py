dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(now_r, now_c):
    q = [(now_r, now_c, 0)]
    visited = list([False] * N for _ in range(N))
    visited[now_r][now_c] = True

    while q:
        r, c, dist = q.pop(0)
        for di in range(4):
            next_r = now_r + dr[di]
            next_c = now_c + dc[di]

            if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
                if sea[next_r][next_c] <= shark_size:
                    visited[next_r][next_c] = True
                    if 0 < sea[next_r][next_c] < shark_size:
                        pass




N = int(input())
sea = list(list(map(int, input().split())) for _ in range(N))

shark_size = 2
fish = []

for i in range(N):
    for j in range(N):
        if 1 <= sea[i][j] <= 6:
            fish.append((i, j))
        elif sea[i][j] == 9:
            sea[i][j] = 0       # 움직일때 막힘 방지
            shark_now = [i, j]  # 현재 위치



