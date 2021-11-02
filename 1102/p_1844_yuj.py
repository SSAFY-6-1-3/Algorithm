from collections import deque
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[-1][-1] = 1
    queue = deque([(n-1, m-1, 1)])
    result = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, cnt = queue.popleft()
        if x == 0 and y == 0:
            result = cnt
            break

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if nx in range(n) and ny in range(m):
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx, ny, cnt+1))
                    visited[nx][ny] = 1

    if result:
        return result
    else:
        return -1
print(solution(maps))