def solution(a, b, g, s, w, t):
    answer = float('inf')
    sta = 0
    end = (10**9) * (10**5) * 4

    while sta <= end :
        mid = (sta + end) // 2
        gold, silver, total = 0, 0, 0

        for i in range(len(g)):
            n_gold, n_silver = g[i], s[i]
            n_wgt, n_time = w[i], t[i]

            move_cnt = mid // (n_time * 2)
            if mid % (n_time * 2) >= n_time:
                move_cnt += 1

            if n_gold < move_cnt * n_wgt :
                gold += n_gold
            else :
                gold += move_cnt * n_wgt

            if n_silver < move_cnt * n_wgt :
                silver += n_silver
            else :
                silver += move_cnt * n_wgt

            if n_gold + n_silver < move_cnt * n_wgt :
                total += n_gold + n_silver
            else :
                total += move_cnt * n_wgt

        if gold >= a and silver >= b and total >= a+b:
            end = mid-1
            answer = min(answer, mid)
        else:
            sta = mid + 1

    return answer




print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))