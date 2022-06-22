from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
portal = {}
for _ in range(N + M):
    i, o = map(int, input().split())
    portal[i] = o


def bfs():
    q = deque([(1, 0)])
    visited = set()

    while q:
        now, cnt = q.popleft()

        for i in range(1, 7):
           next = portal.get(now + i, now + i)
           if next in visited or next not in range(101): continue
           elif next == 100:
               return cnt + 1
           visited.add(next)
           q.append((next, cnt + 1))

print(bfs())


