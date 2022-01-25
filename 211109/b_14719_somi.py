H, W = map(int, input().split())
heights = list(map(int, input().split()))
blocks = [[0] * W for _ in range(H)]
for i in range(W):
    for h in range(heights[i]):
        blocks[h][i] = 1

rain = 0
for r in range(H):
    tmp = 0
    start = False
    for c in range(W):
        if not start and blocks[r][c] == 1:
            start = True
            continue

        if start and blocks[r][c] == 0:
            tmp += 1
            continue

        if start and blocks[r][c] == 1:
            rain += tmp
            tmp = 0

print(rain)


'''
# FAIL!!

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

rain = 0


start = 0
now = 1
end = 0


while now < W:

    while start < W and now < W:

        if blocks[start] < blocks[now]:
            start += 1
            now += 1
        else:
            break

    end = now + 1
    while end < W:
        if blocks[now] <= blocks[end]:
            end += 1
            now += 1
        else:
            break

    for i in range(start + 1, now):
        rain += min(blocks[start], blocks[now]) - blocks[i]

    start = now
    now += 1


print(rain)

'''


