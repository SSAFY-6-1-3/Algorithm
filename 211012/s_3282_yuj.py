import sys
sys.stdin=open('input.txt')

# DP
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    Vs = [0]
    Cs = [0]
    for _ in range(N):
        v, c = map(int, input().split())
        Vs.append(v)
        Cs.append(c)
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(N+1):
        for j in range(K+1):
            if j -Vs[i] >= 0:
                dp[i][j] = max(dp[i-1][j-Vs[i]]+Cs[i], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print('#{}'.format(tc), dp[-1][-1])