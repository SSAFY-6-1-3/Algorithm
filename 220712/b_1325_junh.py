import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    tree[b].append(a)

def bfs(s):
    q = deque([s])
    visited = [False] * (N+1)
    visited[s] = True
    cnt = 1

    while q:
        n = q.popleft()

        for i in tree[n]:
            if visited[i]: continue
            visited[i] = True
            q.append(i)
            cnt += 1

    return cnt


answer = []
answer_max = 0

for i in range(1, N+1):
    tmp = bfs(i)
    if tmp > answer_max:
        answer = [i]
        answer_max = tmp
    elif tmp == answer_max:
        answer.append(i)



print(*answer)