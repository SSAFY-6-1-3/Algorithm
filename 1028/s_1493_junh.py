
dp = [0] * 10000    # 0 1 3 6 10
dp[1] = 1
def get_dp(num):
    if num == 0: return 0
    if not dp[num]:
        dp[num] = get_dp(num-1) + num

    return dp[num]




T = int(input())
for _ in range(T):
    p, q = map(int, input().split())