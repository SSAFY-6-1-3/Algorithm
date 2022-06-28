from collections import deque

dY = (1, 0, -1, 0)  # 하, 우, 상, 좌
dX = (0, 1, 0, -1)

def solution(board):
    answer = 0
    N = len(board)
    visited = [[[float('inf') for _ in range(4)] for _ in range(N)] for _ in range(N)]
    q = [(0, 0, i, 0) for i in range(2)]
    q = deque(q) # (y, x, d, cost)

    while q:
        y, x, d, cost = q.popleft()

        for i in (-1, 0, 1):
            new_d = (4 + d + i) % 4
            new_cost = cost + (600 if i else 100)
            ny, nx = y + dY[new_d], x + dX[new_d]

            if ny not in range(N) or nx not in range(N) or board[ny][nx]: continue

            v_cost = visited[ny][nx][new_d]
            if v_cost <= new_cost: continue

            visited[ny][nx][new_d] = new_cost
            q.append((ny, nx, new_d, new_cost))


    return min(visited[N-1][N-1])


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))