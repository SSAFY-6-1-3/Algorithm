# 임의의 노드에서 각 노드까지의 거리를 측정하여 최대 거리를 가지는 노드는 트리의 지름을 이루는 한 노드이다.
def dfs(node, num):
    global ans
    for n, v in tree[node]:
        if not visited[n]:
            visited[n] = num+v
            dfs(n, num+v)

V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    nodes = list(map(int, input().split()))
    for i in range(1, len(nodes)-1, 2):
        tree[nodes[0]].append([nodes[i], nodes[i+1]])

visited = [0] * (V+1)
visited[1] = 1
dfs(1, 0)
start = visited.index(max(visited))

visited = [0] * (V+1)
visited[start] = 1
dfs(start, 0)
print(max(visited))