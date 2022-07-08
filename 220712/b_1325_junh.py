import sys

input = sys.stdin.readline
N, M = map(int, input().split())
tree = [set() for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    tree[b].add(a)

def dfs(n):
    visited[n] = True
    tmp = {n}
    for i in tree[n]:
        if visited[i]:
            tmp.update(tree[i])
        else:
            tmp.update(dfs(i))
    tree[n].update(tmp)

    return tmp


answer = [0]
for i in range(1, N):
    visited = [0] * (N+1)
    tree[i] = dfs(i)

    if len(tree[i]) > len(tree[answer[0]]):
        answer = [i]
    elif len(tree[i]) == len(tree[answer[0]]):
        answer.append(i)

print(' '.join(map(str, answer)))
print(tree)
