import sys
from collections import deque

input = sys.stdin.readline
# sys.setrecursionlimit(99999)

# def check_leaf(node, depth):
#     global cnt
#     visited[node] = True
#
#     if len(tree[node])==1 and node != 1:
#         cnt += depth
#         return
#
#     for n in tree[node]:
#         if not visited[n]:
#             check_leaf(n, depth+1)

def check_leaf_bfs(tree):
    global cnt
    queue = deque()
    queue.append((1, 0))

    while queue:
        node, depth = queue.popleft()
        visited[node] = True

        if len(tree[node])==1 and node != 1:
            cnt += depth
            continue

        for n in tree[node]:
            if not visited[n]:
                queue.append((n, depth+1))





N = int(input())
tree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

cnt = 0
check_leaf_bfs(tree)

if cnt % 2:
    print('Yes')
else:
    print('No')