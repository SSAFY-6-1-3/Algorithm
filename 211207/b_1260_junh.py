from collections import deque

N, M, V = map(int, input().split())
tree = [[False for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    tree[a][b] = True
    tree[b][a] = True


def dfs(start, N):
    stk = [start]
    visited = []
    while stk:
        node = stk.pop()
        if node in visited:
            continue
        visited.append(node)
        for i in range(N, 0, -1):
            if tree[node][i] and i not in visited:
                stk.append(i)
    return visited

def bfs(start, N):
    q = deque([start])
    visited = [start]
    while q:
        node = q.popleft()
        for i in range(1, N+1):
            if tree[node][i] and i not in visited:
                visited.append(i)
                q.append(i)
    return visited



print(*dfs(V, N))
print(*bfs(V, N))


