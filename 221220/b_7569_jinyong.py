import sys

custom_input = sys.stdin.readline

M, N, H = map(int, custom_input().split())

lst = [[list(map(int, custom_input().split())) for _ in range(N)] for _ in range(H)]


def solution(tomatoes, n, m, h):
    answer = 0
    dr = [-1, 1, 0, 0, 0, 0]
    dc = [0, 0, -1, 1, 0, 0]
    dk = [0, 0, 0, 0, -1, 1]
    queue = []
    rear = 0

    for k in range(h):
        for r in range(n):
            for c in range(m):

                if tomatoes[k][r][c] == 1:
                    queue.append((k, r, c))
                    rear += 1

    head = 0

    while head < rear:
        ck, cr, cc = queue[head]
        head += 1

        for i in range(6):
            nk, nr, nc = ck + dk[i], cr + dr[i], cc + dc[i]

            if nk < 0 or nk >= h or nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if tomatoes[nk][nr][nc]:
                continue

            queue.append((nk, nr, nc))
            tomatoes[nk][nr][nc] = tomatoes[ck][cr][cc] + 1
            rear += 1

    for k in range(h):
        for r in range(n):
            for c in range(m):
                if tomatoes[k][r][c] == 0:
                    return -1

                answer = max(answer, tomatoes[k][r][c])

    return answer - 1


print(solution(lst, N, M, H))
