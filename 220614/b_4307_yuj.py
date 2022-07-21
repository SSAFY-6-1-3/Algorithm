T = int(input())
for _ in range(T):
    l, num = map(int, input().split())
    low, high = 0, 0
    ants = []
    for _ in range(num):
        ants.append(int(input()))
    for ant in ants:
        if l-ant > ant:
            low = max(low, ant)
            high = max(high, l-ant)
        else:
            low = max(low, l-ant)
            high = max(high, ant)

    print(low, high)