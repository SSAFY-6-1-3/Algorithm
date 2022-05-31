K = int(input())
field = list()

width = 0
width_idx = 0
height = 0
height_idx = 0

for i in range(6):
    direction, length = map(int, input().split())
    field.append([direction, length])
    if direction == 1 or direction == 2:  # 동 서
        if width < length:
            width = length
            width_idx = i
    else:                                 # 남 북
        if height < length:
            height = length
            height_idx = i

idx_set = set()
for j in range(-1, 2):  # 가장 긴 변과 인접한 변 저장
    idx_set.add((width_idx + j) % 6)
    idx_set.add((height_idx + j) % 6)

small_idx = list(set(k for k in range(6)) - idx_set)
big = width * height
small = field[small_idx[0]][1] * field[small_idx[1]][1]

print((big - small) * K)