dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def move():
    q = [[0, 0, 0]]  #[r, c, break 여부]

    visited[0][0][0] = 1

    while q:
        r, c, broken = q.pop(0)

        if r == N - 1 and c == M - 1:
            return visited[r][c][broken]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc][broken]:
                if maze[nr][nc] == 0:  # 길 인 경우
                    q.append([nr, nc, broken])
                    visited[nr][nc][broken] = visited[r][c][broken] + 1

                elif maze[nr][nc] == 1 and not broken:  # 벽이지만, 뚫을 기회가 있는 경우,
                    q.append([nr, nc, 1])
                    visited[nr][nc][1] = visited[r][c][0] + 1
    return -1


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = list([[0] * 2 for _ in range(M)] for _ in range(N))

print(move())


"""

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def move(r, c, distance, broken):
    global min_distance
    if distance > min_distance:
        return

    if r == N-1 and c == M-1:
        if distance < min_distance:
            min_distance = distance
        return

    visited[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if maze[nr][nc] == 0:
                move(nr, nc, distance + 1, broken)
            elif maze[nr][nc] == 1 and not broken:
                move(nr, nc, distance + 1, True)

    visited[r][c] = False


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

min_distance = 1000001
move(0, 0, 1, False)
if min_distance == 1000001:
    print(-1)
else:
    print(min_distance)

"""
