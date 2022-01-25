import sys
input = sys.stdin.readline

def del_line(N, lines):
    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if lines[i][1] > lines[j][1]:
                dp[i] = max(dp[i], dp[j]+1)
    return N-max(dp)


N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()
print(del_line(N, lines))
