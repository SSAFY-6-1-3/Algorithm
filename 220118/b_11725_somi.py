def find_child():
    q = [1]  # 루트노드가 1
    while q:
        parent = q.pop(0)
        for c in tree[parent]:  # 연결된 노드 중
            if not parents[c]:  # 아직 부모 노드가 없는 경우
                parents[c] = parent
                q.append(c)


N = int(input())
parents = [0 for _ in range(N + 1)]
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)


find_child()
print(*parents[2:], sep="\n")  # 2번 노드부터 출력