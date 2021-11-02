def solution(maps):
    N = len(maps)
    M = len(maps[0])

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    q = [(0, 0, 1)]


    while q:
        r, c, cnt = q.pop(0)
        if r == N - 1 and c == M - 1:  # 도착하면 return
            return cnt

        for di in range(4):
            nr, nc = r + dr[di], c + dc[di]
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc]:  # 인덱스가 범위 내이고, 벽이 아닌 경우
                q.append((nr, nc, cnt + 1))
                maps[nr][nc] = 0  # 벽으로 만들기

    return -1  # 도착못하면 -1 반환