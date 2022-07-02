T = int(input())
for _ in range(T):
    n = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))

    for c in range(1, n):
        if c == 1:
            stickers[0][c] += stickers[1][0]
            stickers[1][c] += stickers[0][0]
        else:
            stickers[0][c] += max(stickers[1][c - 2], stickers[1][c - 1])
            stickers[1][c] += max(stickers[0][c - 2], stickers[0][c - 1])
    print(max(stickers[0][n - 1], stickers[1][n - 1]))