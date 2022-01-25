import sys
sys.stdin = open('s_3752_input.txt')

def dp_solut(N, points):
    dp = [0] * 10001
    dp[0] = 1
    reach = 1
    for n in points:
        for i in range(reach, -1, -1):
            if dp[i]:
                dp[i+n] = 1
                reach = max(reach, i+n+1)

    return sum(dp)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    points = sorted(map(int, input().split()))

    print('#{} {}'.format(tc, dp_solut(N, points)))