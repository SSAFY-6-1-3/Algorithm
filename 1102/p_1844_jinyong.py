def solution(maps):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # n x m 크기의 2차원 배열인데 n : 행, m : 열 의 크기를 나타낸다.
    m = len(maps[0])
    n = len(maps)

    queue = [[] for _ in range(n * m * 10)]
    head = 0
    rear = 1
    visited = {(0, 0)}
    queue[0] = [0, 0, 1]

    while head < rear:
        r, c, cnt = queue[head]
        head += 1

        if [r, c] == [n-1, m-1]:
            return cnt

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if maps[nr][nc] == 0:
                continue

            if (nr, nc) in visited:
                continue

            visited.add((nr, nc))
            queue[rear] = [nr, nc, cnt + 1]
            rear += 1

    return -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
