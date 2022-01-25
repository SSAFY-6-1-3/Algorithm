dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def check_group(x, y):
    global worm

    stack = [(x, y)]
    while stack:
        r, c = stack.pop()

        for di in range(4):
            nr, nc = r + dr[di], c + dc[di]
            if [nr, nc] in cabbage and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
    worm += 1



T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())  # M : 가로길이 / N : 세로길이 / K : 배추 개수
    cabbage = [list(map(int, input().split())) for _ in range(K)]  # 배추 위치 인덱스
    visited = [[0] * N for _ in range(M)]  # 땅 모양 visit 처리


    worm = 0  # 필요한 지렁이 개수
    for c in cabbage:  # 모든 배추를 확인
        x, y = c[0], c[1]
        if not visited[x][y]:
            visited[x][y] = 1
            check_group(x, y)

    print(worm)

