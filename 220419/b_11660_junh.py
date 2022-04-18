import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mat = [[0]*(N+1)]
dp = [[0]*(N+1) for _ in range(N+1)]


for i in range(1, N+1):
    mat.append([0]+list(map(int, input().split())))
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i][j]

pntss = [list(map(int, input().split())) for _ in range(M)]

def calc(pnts, mat):
    x1, y1, x2, y2 = pnts

    return dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]

prt = ''
for pnts in pntss:
    prt += str(calc(pnts, mat))+'\n'
print(prt)