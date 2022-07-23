def solution(n, computers):
    answer = 0
    checked = [0] * n

    def check(s):
        for j in range(n):
            if computers[s][j] and not checked[j]:
                checked[j] = 1
                check(j)

    for i in range(n):
        if not checked[i]:
            answer += 1
            checked[i] = 1
            check(i)

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))