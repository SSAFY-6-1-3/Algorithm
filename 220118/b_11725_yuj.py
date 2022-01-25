import sys
input=sys.stdin.readline
from collections import deque

def find():
    deq = deque([1])
    while deq:
        i = deq.popleft()
        for j in tree[i]:
            if not visited[j]:
                result[j] = i
                visited[j] = 1
                deq.append(j)

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0] * (N+1)
result = [0] * (N+1)
find()
for k in range(2, N+1):
    print(result[k])