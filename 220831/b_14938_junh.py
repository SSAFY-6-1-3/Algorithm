import sys
from collections import deque

input = sys.stdin.readline
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[100]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = graph[b][a] = l


def check(s):
    q = deque([(s)])
    dists = [1501] * (n+1)
    dists[s] = 0
    while q:
        a = q.popleft()
        dist = dists[a]
        for b in range(1, n+1):
            if dist + graph[a][b] >= dists[b]: continue
            if dist + graph[a][b] <= m:
                dists[b] = dist + graph[a][b]
                q.append(b)

    rtn = 0
    for i in range(1, n+1):
        if dists[i] < 1501:
            rtn += items[i]

    return rtn


answer = 0
for i in range(1, n+1):
    answer = max(answer, check(i))
print(answer)