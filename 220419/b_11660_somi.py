def get_sum(x1, y1, x2, y2):
    area_sum = 0
    for r in range(x1-1, x2):
        for c in range(y1-1, y2):
            area_sum += arr[r][c]
    return area_sum


N, M = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(get_sum(x1, y1, x2, y2))