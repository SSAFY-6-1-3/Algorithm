def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    min_cnt = len(set(lottos) & (set(win_nums)))  # 교집합 intersection
    max_cnt = lottos.count(0) + min_cnt
    answer = [rank[max_cnt], rank[min_cnt]]
    return answer