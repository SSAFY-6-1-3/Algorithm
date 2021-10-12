import sys

input = sys.stdin.readline

def travel(now, cnt, cost):
    global min_cost
    if cost > min_cost:
        return
    if cnt == N:
        if tree[now][vistited[0]]:
            min_cost = min(min_cost, cost + tree[now][vistited[0]])
        return

    for nxt in range(N):
        if nxt not in vistited and tree[now][nxt] > 0:     # 행렬식으로 하다가 처음 시작한 곳 저장하기 위해 리스트 사용
            vistited.append(nxt)
            travel(nxt, cnt+1, cost + tree[now][nxt])
            vistited.pop()


N = int(input())
tree = [list(map(int, input().split())) for _ in range(N)]
vistited = []
min_cost = sum(map(sum, tree))
for i in range(N):
    vistited.append(i)
    travel(i, 1, 0)
    vistited.pop()
print(min_cost)