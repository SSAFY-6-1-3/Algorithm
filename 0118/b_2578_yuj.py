def find(num):
    for x in range(5):
        for y in range(5):
            if num == bingo[x][y]:
                r[x].append(cnt)
                c[y].append(cnt)
                if x == y:
                    diag[0].append(cnt)
                if x + y == 4:
                    diag[1].append(cnt)
                return


bingo = [list(map(int, input().split())) for _ in range(5)]
res = [list(map(int, input().split())) for _ in range(5)]

r = [[] for _ in range(5)]
c = [[] for _ in range(5)]
diag = [[] for _ in range(2)]
cnt = 0

for i in range(5):
    for j in range(5):
        cnt += 1
        find(res[i][j])


ans = []
ans.append(diag[0][4])
ans.append(diag[1][4])
for k in range(5):
    ans.append(r[k][4])
    ans.append(c[k][4])
ans.sort()
print(ans[2])