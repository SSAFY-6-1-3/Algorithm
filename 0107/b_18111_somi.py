def flatten(height):
    time = 0
    for key in heights.keys():
        if key < height:
            time += (height - key) * heights[key]
        elif key > height:
            time += 2 * (key - height) * heights[key]
    return time


N, M, B = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

heights = {}  # {땅 높이 : 개수}
for i in range(N):
    for j in range(M):
        if area[i][j] in heights:
            heights[area[i][j]] += 1
        else:
            heights[area[i][j]] = 1


# height_list = sorted(heights.items(), key=lambda x: x[0])

sum_height = sum(map(sum, area))  # 현재 총 블록 개수
min_time = float('inf')
ans = 0

for h in range(257):  # 땅 높이는 0 ~ 256 가능
    need = (h * N * M) - sum_height
    if B - need >= 0:
        t = flatten(h)
        if min_time > t:
            min_time = t
            ans = h
        elif min_time == t:
            if ans < h:
                ans = h

print(min_time, ans)

