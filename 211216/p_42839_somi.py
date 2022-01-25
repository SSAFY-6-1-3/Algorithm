import math

def is_prime(num):
    if num in [0, 1]:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


def solution(numbers):
    ans = 0
    n = len(numbers)

    result = set()

    def permutation(n, m, k):  # n 개의 숫자 중 m 개 선택할 때, k 번째 선택하기
        if k == m:
            number = int(''.join(p))
            if is_prime(number):
                result.add(number)

        else:
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    p[k] = numbers[i]
                    permutation(n, m, k + 1)
                    used[i] = False

    for m in range(1, n + 1):
        p = [0] * m
        used = [False] * n
        permutation(n, m, 0)
    return len(result)

print(solution('011'))