def solution(n):
    answer = ''
    nums = [1, 2, 4]
    while True:
        if n < 4:
            answer += str(nums[n - 1])
            break
        if n % 3 == 0:
            answer += '4'
            n = n // 3 - 1
        else:
            answer += str(n % 3)
            n //= 3

    return answer[::-1]