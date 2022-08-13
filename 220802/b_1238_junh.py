import sys
from collections import deque

input = sys.stdin.readline
N, M, X = map(int, input().split())
routes = [[] for _ in range(N+1)]
dists = [[100000] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    routes[a].append((b, t))
    dists[a][b] = t

def bfs(start):
    q = deque([n for n, d, in routes[start]])
    dists[start][start] = 0
    while q:
        now = q.popleft()
        for nxt, d in routes[now]:
            if dists[start][nxt] <= dists[start][now] + d:
                continue

            dists[start][nxt] = dists[start][now] + d
            q.append(nxt)

for i in range(1, N+1):
    bfs(i)

max_time = 0
for i in range(1, N+1):
    tmp = dists[i][X] + dists[X][i]
    max_time = max(max_time, tmp)

print(max_time)

# https://velog.io/@do0134/Python-1238-파티

# from heapq import *
#
#
# n, m, x = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# graph_inv = [[] for _ in range(n + 1)]
# for _ in range(m):
#     s, e, t = map(int, input().split())
#     graph[s].append((e, t))
#     graph_inv[e].append((s, t))
# INF = float('inf')
# dist = [INF] * (n + 1)
# dist[x] = 0
# point = [(0, x)]
# while point:
#     c, idx = heappop(point)
#     if dist[idx] < c:
#         continue
#     for adj, ex in graph[idx]:
#         if dist[adj] > c + ex:
#             dist[adj] = c + ex
#             heappush(point, (dist[adj], adj))
# dist_inv = [INF] * (n + 1)
# dist_inv[x] = 0
# point = [(0, x)]
# while point:
#     c, idx = heappop(point)
#     if dist_inv[idx] < c:
#         continue
#     for adj, ex in graph_inv[idx]:
#         if dist_inv[adj] > c + ex:
#             dist_inv[adj] = c + ex
#             heappush(point, (dist_inv[adj], adj))
# ans = 0
# for idx in range(1, n + 1):
#     if ans < dist[idx] + dist_inv[idx]:
#         ans = dist[idx] + dist_inv[idx]
# print(ans)

