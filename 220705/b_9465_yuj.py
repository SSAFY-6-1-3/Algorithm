T = int(input())

for _ in range(T):
    n = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    if n > 1:
        dp = [0] * n
        dp[0] = max(stickers[0][0], stickers[1][0])

        for i in range(1, n):
            if i == 1:
                stickers[0][i] += stickers[1][i-1]
                stickers[1][i] += stickers[0][i - 1]
            else:
                stickers[0][i] += max(stickers[1][i-1], dp[i-2])
                stickers[1][i] += max(stickers[0][i-1], dp[i-2])
            dp[i] = max(stickers[0][i], stickers[1][i])
        print(dp[-1])
    else:
        print(max(stickers[0][0], stickers[1][0]))