def dfs():
    global move
    visited = list([False for _ in range(N + 1)] for _ in range(N + 1))
    s = [(0, 1, 0)]

    while s:
        before, now, dist = s.pop(-1)
        move = max(move, dist)

        for i in range(1, N + 1):
            if roads[now][i] and not visited[now][i]:
                s.append((now, i, dist + roads[now][i]))
                visited[now][i] = True
                visited[i][now] = True

N = int(input())
roads = list([0 for _ in range(N + 1)] for _ in range(N + 1))
for _ in range(N - 1):
    A, B, C = map(int, input().split())
    roads[A][B] = C
    roads[B][A] = C

move = 0

dfs()
print(move)