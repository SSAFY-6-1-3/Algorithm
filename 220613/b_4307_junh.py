
T = int(input())


def simul(ants):
    longest = 0
    shortest = 0

    for ant in ants:
        if ant > l-ant:
            longer, shorter = ant, l-ant
        else:
            longer, shorter = l-ant, ant

        longest = max(longest, longer)
        shortest = max(shortest, shorter)
    return longest, shortest

for _ in range(T):
    l, n = map(int, input().split())
    ants = [int(input()) for _ in range(n)]
    min_time, max_time = l, 0

    lo, sh = simul(ants)
    min_time = min(min_time, sh)
    max_time = max(max_time, lo)

    print(min_time, max_time)