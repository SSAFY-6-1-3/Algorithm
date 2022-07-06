
T = int(input())


def sero(num):
    if num: return 0
    return 1

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    answer = max(max(stickers[0]), max(stickers[1]))
    if n != 1:
        dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]
        dp[0][1], dp[1][1] = stickers[1][0] + stickers[0][1], stickers[0][0] + stickers[1][1]

        for j in range(2, n):
            for i in range(2):
                dp[i][j] = max(dp[sero(i)][j-1], dp[sero(i)][j-2]) + stickers[i][j]

        answer = max(dp[0][n-1], dp[1][n-1])

    print(answer)

