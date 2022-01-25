from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    q= deque([(a, 0)])
    visited = [False] * (N+1)
    visited[a] = True

    while q:
        node, cnt = q.popleft()

        for next in range(1, N+1):
            if tree[node][next] and not visited[next]:
                visited[next] = True
                if next == b:
                    return cnt+1
                q.append((next, cnt+1))


N = int(input())
a, b = map(int, input().split())
tree = [[False]*(N+1) for _ in range(N+1)]
M = int(input())
for _ in range(M):
    p, c = map(int, input().split())
    tree[p][c] = True
    tree[c][p] = True
print(bfs(a, b))