import sys
from collections import deque

sys.stdin = open('s_7465.txt')

def check(p):
    q = deque([p])

    while q:
        person = q.popleft()
        visited[person] = True

        for ne in tree[person]:
            if not visited[ne] and ne not in q:
                q.append(ne)





T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    answer = 0
    for p in range(1, N+1):
        if not visited[p]:
            check(p)
            answer += 1
    print('#{} {}'.format(tc, answer))
