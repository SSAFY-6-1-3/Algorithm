N = int(input())
house = [0] * 1001

start = 1001
end = 0
maxH = 0
maxIdx = 0
for _ in range(N):
    L, H = map(int, input().split())
    house[L] = H
    start = min(start, L)
    end = max(end, L)
    if maxH < H:
        maxH = H
        maxIdx = L

height = 0
h_sum = 0
for idx in range(start, maxIdx + 1):
    height = max(height, house[idx])
    h_sum += height

height = 0
for idx in range(end, maxIdx, -1):
    height = max(height, house[idx])
    h_sum += height
print(h_sum)
