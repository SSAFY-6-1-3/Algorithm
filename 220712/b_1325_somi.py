# 시간초과 pypy 통과

import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    visited = [False for _ in range(N + 1)]
    visited[start] = True
    q = deque([start])
    cnt = 1
    while q:
        now = q.popleft()
        for next in trusted[now]:
            if not visited[next]:
                q.append(next)
                cnt += 1
                visited[next] = True

    return cnt


N, M = map(int, input().split())
trusted = [list() for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    trusted[B].append(A)

ans = []
max_cnt = 0
for i in range(1, N + 1):
    cnt = bfs(i)

    if max_cnt < cnt:
        max_cnt = cnt
        ans = [i]
    elif max_cnt == cnt:
        ans.append(i)

print(' '.join(str(num) for num in ans))

