def find_p(person):
    for p in tree[person]:
        if not visited[p]:
            visited[p] = visited[person] + 1
            find_p(p)


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

visited = [0] * (n + 1)
find_p(p1)

ans = 0
if visited[p2] == 0:
    ans = -1
else:
    ans = visited[p2]

print(ans)
