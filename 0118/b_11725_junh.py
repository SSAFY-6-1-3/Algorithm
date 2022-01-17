import sys
from collections import deque

input = sys.stdin.readline

def check_parent(tree, N):
    q = deque([1])

    while q:
        a = q.popleft()
        while tree[a]:
            b = tree[a].pop()
            parent_of[b] = a
            tree[b].remove(a)
            q.append(b)


N = int(input())
tree = [[] for _ in range(N+1)]     # 인접 행렬 메모리 초과
parent_of = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

check_parent(tree, N)

for i in range(2, len(tree)):
    print(parent_of[i])
