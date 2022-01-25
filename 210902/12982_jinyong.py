def solution(d, budget):
    answer = 0
    d.sort()
    d_sum = 0
    for ele in d:
        d_sum += ele
        if d_sum <= budget:
            answer += 1
        else:
            break
    return answer
