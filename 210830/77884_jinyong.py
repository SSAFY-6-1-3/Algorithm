def solution(left, right):
    answer = 0

    for num in range(left, right + 1):  # 약수의 개수가 짝수 => 제곱근 != 정수
        answer += num if (num ** 0.5) % 1 else -num
    return answer


print(solution(13, 17))
