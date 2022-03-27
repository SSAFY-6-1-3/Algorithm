def solution(n):
    num = {1 : '1', 2: '2', 0: '4'}
    answer = ''

    while n > 0:
        n, mod = divmod(n, 3)

        if mod == 0:
            n -= 1
        answer += str(num[mod])
    return answer[::-1]

print(solution(10))