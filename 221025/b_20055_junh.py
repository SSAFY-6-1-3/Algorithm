
N, K = map(int, input().split())
durab = list(map(int, input().split()))
robots = [0] * N

broken = 0
for i in range(N * 2):
    if not durab[i]:
        broken += 1

level = 1
start = 1
while True:
    durab = [durab[-1]] + durab[:(N*2) - 1]
    robots = [0] + robots[:N-1]
    robots[-1] = 0
    for i in range(N-2, -1, -1):
        if robots[i] and not robots[i+1] and durab[i+1]:
            robots[i] = 0
            durab[i+1] -= 1
            if durab[i+1] == 0:
                broken += 1
            if i != N - 2:
                robots[i+1] = 1
    if durab[0]:
        robots[0] = 1
        durab[0] -= 1
        if not durab[0]:
            broken += 1
    if broken >= K:
        break
    level += 1
print(level)






    # for i in range(start, len(robots)):
    #     p = robots[i].place + 1
    #     if p == N * 2:
    #         p = 0
    #
    #     if belt[p] == 0 and durab[p]:
    #         durab[p] -= 1
    #         belt[p] = robots[i].number
    #         belt[(robots[i]).place] = 0
    #         robots[i].place = p





