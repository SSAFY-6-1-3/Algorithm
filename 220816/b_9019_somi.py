# pypy 통과
import sys
input = sys.stdin.readline
from collections import deque


def bfs(A, B):
    q = deque()
    q.append((A, ''))
    while q:
        now_num, command = q.popleft()
        if now_num == B:
            return command

        D = (now_num * 2) % 10000
        S = (now_num - 1) % 10000
        d1, d2 = divmod(now_num, 1000)
        L = (d2 * 10) + d1
        d3, d4 = divmod(now_num, 10)
        R = (d4 * 1000) + d3

        dslr = {"D":D, "S":S, "L":L, "R":R}
        for c, next_num in dslr.items():
            if not visited[next_num]:
                q.append((next_num, command + c))
                visited[next_num] = True


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10001
    visited[A] = True
    print(bfs(A, B))

