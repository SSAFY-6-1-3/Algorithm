# nCr = n-1Cr-1 + n-1Cr
'''
n = 4
comb = [[0C0, 0, 0, 0, 0],[1C0, 1C1, 0, 0, 0],[2C0, 2C1, 2C2, 0, 0], [3C0, 3C1, 3C2, 3C3, 0], [4C0, 4C1, 4C2, 4C3, 4C4]
'''

n, m = map(int, input().split())
comb = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    comb[i][0] = 1  # nC0 = 1
    comb[i][i] = 1  # nCn = 1

for j in range(2, n + 1):
    for k in range(1, j):  # nC1 ~ nCn-1
        comb[j][k] = comb[j - 1][k - 1] + comb[j - 1][k]
print(comb[n][m])