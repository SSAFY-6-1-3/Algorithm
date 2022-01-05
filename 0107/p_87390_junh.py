def solution(n, left, right):
    answer = []

    start = left//n
    end = right//n + 1
    for i in range(start+1, end+1):
        for j in range(1, n+1):
            if j<i:
                answer.append(i)
            else:
                answer.append(j)

    return answer[left%n : right - left//n*n + 1]

print(solution(3, 2, 5))
print(solution(4, 7, 14))
