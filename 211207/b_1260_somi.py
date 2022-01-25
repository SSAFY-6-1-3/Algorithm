def DFS():
    visited = [V]
    stack = []
    for i in range(N, -1, -1):
        if roads[V][i]:
            stack.append(i)

    while stack:
        nextV = stack.pop()
        if nextV not in visited:
            visited.append(nextV)
            for j in range(N, -1, -1):
                if roads[nextV][j]:
                    stack.append(j)
    return visited


def BFS():
    visited = [V]
    q = []

    for i in range(N + 1):
        if roads[V][i]:
            q.append(i)

    while q:
        v = q.pop(0)
        if v not in visited:
            visited.append(v)

            for j in range(N + 1):
                if roads[v][j]:
                    q.append(j)

    return visited


N, M, V = map(int, input().split())
roads = list([False for _ in range(N + 1)] for _ in range(N + 1))
for _ in range(M):
    a, b = map(int, input().split())
    roads[a][b] = True
    roads[b][a] = True

print(*DFS())
print(*BFS())