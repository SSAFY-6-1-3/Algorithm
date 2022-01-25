import sys
sys.stdin=open('input.txt')
from collections import deque

# 트리로 풀 필요 x
# 인접 행렬에서 bfs로 찾아나가기(p1 -> p2)
def bfs():
    people = deque([(p1, 0)])

    while people:
        person, cnt = people.popleft()
        if person == p2:
            return cnt
        for j in range(1, n + 1):
            if family[person][j] == 1:
                people.append((j, cnt+1))
                family[person][j] = 0
                family[j][person] = 0


n = int(input())
p1, p2 = map(int, input().split())
family = [[0] * (n+1) for _ in range(n+1)]      # 연결관계
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    family[x][y] = 1
    family[y][x] = 1

result = bfs()
if result:
    print(result)
else:                                            # 서로 연결된 친척관계가 아닌 경우
    print(-1)

