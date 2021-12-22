def solution(lottos, win_nums):
    ranks = [6, 6, 5, 4, 3, 2, 1]

    worst = len(set(lottos).intersection(set(win_nums)))
    best = worst
    for lotto in lottos:
        if not lotto:
            best += 1

    return [ranks[best], ranks[worst]]



print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))