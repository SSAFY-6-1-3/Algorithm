# pypy로 통과
from collections import deque

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(num):
        global visited

        que = deque([num])
        while que:
            now = que.popleft()
            check = 3 - visited[now]
            for node in graph[now]:
                if not visited[node]:
                    visited[node] = check
                    que.append(node)
                else:
                    if visited[node] != check:
                        return 0
        return 1

    for i in range(1, V+1):
        if not visited[i]:
            visited[i] = 1
            if not bfs(i):
                print('NO')
                break
    else:
        print('YES')
