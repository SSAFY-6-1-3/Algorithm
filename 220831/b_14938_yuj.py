# 최단경로 구하기 (플로이드-워셜 알고리즘)
# 수색범위보다 짧은 경로 모두 확인
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
INF = float('inf')
field = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    field[a][b] = l
    field[b][a] = l

# 자기 자신으로 돌아오는 경로는 0으로 설정
for s in range(1, n+1):
    field[s][s] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            field[i][j] = min(field[i][j], field[i][k] + field[k][j])

ans = 0
for r in range(1, n+1):
    item = 0
    for c in range(1, n + 1):
        if field[r][c] <= m:
            item += items[c]
    ans = max(ans, item)

print(ans)