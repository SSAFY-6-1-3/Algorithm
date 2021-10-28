import sys

# sys.stdin = open('s_1493.txt')

def calc_and(n):
    i = 0
    while dp[i]<n:
        i+=1

    y = dp[i] - n
    x = i-y
    y+=1
    return y, x

def calc_sharp(y, x):
    i = y +x -1
    n = dp[i] -y +1
    return n




dp = [0] * 10000    # 0 1 3 6 10
for i in range(1, 10000):
    dp[i] = dp[i - 1] + i

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())
    and_p, and_q = calc_and(p), calc_and(q)
    y, x = and_p[0]+and_q[0], and_p[1]+and_q[1]
    print('#{} {}'.format(tc, calc_sharp(y, x)))