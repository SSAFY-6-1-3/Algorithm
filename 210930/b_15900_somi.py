from sys import stdin

N = int(input())

tree = [[] for _ in range(N + 1)]  # tree 생성하기
for i in range(N-1):
    b1, b2 = map(int, stdin.readline().split())
    tree[b1].append(b2)
    tree[b2].append(b1)

# print(tree)
# [[], [8, 4, 3], [], [1], [1, 7, 6], [6], [4, 5], [4], [1]]


visited = [0] * (N + 1) # 1번 노드 ~ N 노드 방문 했는 지 체크

stack = [(1, 0)]  # (node 번호, 1번노드와의 거리)
counts = []       # 각 리프노드에서 1번 노드까지의 거리를 저장

while stack:
    node, count = stack.pop()

    visited[node] = 1

    if len(tree[node]) == 1 and node != 1:   # 맨 마지막 노드(리프 노드)인 경우

        counts.append(count)   # 이제까지 합산한 거리를 counts 리스트에 저장

    else:
        for i in tree[node]:  # 해당 노드에 연결 된 노드에 대해서
            if not visited[i]: # 아직 방문 안했다면
                stack.append((i, count + 1))  # stack에 넣어주고, 거리 +1


if sum(counts) % 2: # 홀수라면: 성원이 차례에서 말 다 없어짐
    print('Yes')
else:
    print('No')
