import sys
from collections import deque


input = sys.stdin.readline
V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(V):
    nums = list(map(int, input().split()))
    a = nums[0]
    for i in range(1, len(nums)-1, 2):
        tree[a].append((nums[i], nums[i+1]))


def bfs(start):
    q = deque([start])
    visited = [float('inf')] * (V+1)
    visited[0] = visited[start] = 0

    while q:
        a = q.popleft()
        dist = visited[a]

        for b, d in tree[a]:
            if visited[b] > dist + d:
                visited[b] = dist + d
                q.append(b)

    return visited


farthest = max(enumerate(bfs(1)), key= lambda x:x[1])[0]
print(max(bfs(farthest)))