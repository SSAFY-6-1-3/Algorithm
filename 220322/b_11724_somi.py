import sys
input = sys.stdin.readline

def connection(node):
    q = [node]

    while q:
        now = q.pop(0)
        for n in graph[now]:
            if not visited[n]:
                visited[n] = True
                q.append(n)
                
N, M = map(int, input().split())

graph = [list() for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
ans = 0
for i in range(1, N + 1):
    if not visited[i]:
        visited[i] = True
        connection(i)
        ans += 1

print(ans)