import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))


def bfs(start):
    q = deque([start])
    visited = [-1] * (n+1)
    visited[start] = 0
    farthest = (0, 0)

    while q:
        now = q.popleft()
        for nxt, wgt in tree[now]:

            if visited[nxt] == -1 or visited[nxt] > visited[now] + wgt:
                visited[nxt] = visited[now] + wgt
                if visited[nxt] > farthest[1]:
                    farthest = (nxt, visited[nxt])
                q.append(nxt)

    return farthest


start = bfs(1)[0]
print(bfs(start)[1])
