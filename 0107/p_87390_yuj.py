def solution(n, left, right):
    answer = []
    for idx in range(left, right+1):
        q, r = idx // n, idx % n
        if r <= q:
            answer.append(q+1)
        else:
            answer.append(r+1)
    return answer

n, left, right = 4, 7, 14
print(solution(n, left, right))