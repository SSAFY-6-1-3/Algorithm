import sys
from collections import deque


def check():
    colors = [None] * (V+1)

    def bfs(start):
        colors[start] = True
        q = deque([start])

        while q:
            a = q.popleft()
            clr = colors[a]

            for b in graph[a]:
                if colors[b] is None:
                    colors[b] = not clr
                    q.append(b)
                elif colors[b] == clr:
                    return False
                elif colors[b] != clr:
                    continue
        return True

    for i in range(1, V+1):
        if colors[i] is None:
            if not bfs(i):
                return "NO"

    return "YES"

input = sys.stdin.readline
K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(check())
