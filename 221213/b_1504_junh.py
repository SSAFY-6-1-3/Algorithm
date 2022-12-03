from collections import deque

N, E = map(int, input().split())
tree = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))
v1, v2 = map(int, input().split())

def dist(s, e):
    q = deque([s])
    visited = [float('inf')] * (N+1)
    visited[s] = 0

    while q:
        a = q.popleft()
        dist = visited[a]
        for b, c in tree[a]:
            if visited[b] > dist + c:
                visited[b] = dist + c
                q.append(b)

    return visited[e]

answer = dist(v1, v2) + min(dist(1, v1) + dist(v2, N), dist(1, v2) + dist(v1, N))
if answer == float('inf'):
    answer = -1

print(answer)