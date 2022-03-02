def solution(orders, course):

    def comb(start, order, result):
        nonlocal dict

        if len(result) == N:
            if not dict.get(result):
                dict[result] = 1
            else:
                dict[result] += 1

        for i in range(start, len(order)):
            comb(i+1, order, result+order[i])

    answer = []

    for N in course:

        dict = {}

        for order in orders:
            comb(0, sorted(order), "")

        cands = sorted(dict.items(), key= lambda x: -x[1])

        if not cands: continue
        max_n = cands[0][1]
        if max_n <= 1: continue
        for cand in cands:
            if cand[1] == max_n:
                answer.append(cand[0])
            else:
                break

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))