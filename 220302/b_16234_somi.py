# Python으로는 시간초과  pypy3로 통과

def move(i, j):
    global is_finished
    open = [(i, j)]  # 국경선 열리는 국가
    open_nations = [(i, j)]
    people = nations[i][j]  # 연합 인구 수
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while open:
        r, c = open.pop(0)
        for i in range(4):
            if 0 <= r + d[i][0] < N and 0 <= c + d[i][1] < N:
                nr = r + d[i][0]
                nc = c + d[i][1]
                if L <= abs(nations[r][c] - nations[nr][nc]) <= R:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        open.append((nr, nc))
                        open_nations.append((nr, nc))
                        people += nations[nr][nc]
    if len(open_nations) >= 2:
        is_finished = False
        people //= len(open_nations)
        for n in open_nations:
            nations[n[0]][n[1]] = people



N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]

day = 0  # 며칠 걸리는지
while True:
    is_finished = True  # 인구 이동이 끝났는 지 여부
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                move(i, j)

    if not is_finished:
        day += 1
    else:
        break

print(day)


