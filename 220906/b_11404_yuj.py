n = int(input())
m = int(input())
inf = float('inf')
result = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if result[a][b] > c:
        result[a][b] = c

for m in range(n+1):
    result[m][m] = 0

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if i != j and result[i][k]+result[k][j] < result[i][j]:
                result[i][j] = result[i][k]+result[k][j]

for r in range(1, n+1):
    for c in range(1, n+1):
        if result[r][c] == inf:
            print(0, end=" ")
        else:
            print(result[r][c], end=" ")
    print()