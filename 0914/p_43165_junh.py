def solution(numbers, target):
    answer = 0
    num_len = len(numbers)

    def recur(idx, n_sum):
        nonlocal answer
        if idx == num_len:
            if n_sum == target:
                answer += 1
            return

        for c in range(2):
            if c :
                recur(idx + 1, n_sum + numbers[idx])
            else :
                recur(idx + 1, n_sum - numbers[idx])

    recur(0, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))