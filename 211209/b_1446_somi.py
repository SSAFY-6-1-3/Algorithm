N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]
shortcuts.sort(key=lambda x: (x[0], x[1], x[2]))

road = [i for i in range(D + 1)]

for shortcut in shortcuts:
    start, end, dist = shortcut
    if end <= D:
        road[end] = min(road[start] + dist, road[end])

    for j in range(end, D + 1):
        road[j] = min(road[j - 1] + 1, road[j])

print(road[D])
