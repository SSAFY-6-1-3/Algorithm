def solution(numbers):
    answer = []
    length = len(numbers)
    powers = [[numbers[i], 0] for i in range(length)]

    for i in range(length):
        num = str(numbers[i])
        n_len = len(num)
        pow = ''
        for k in range(4):
            pow += num[k%n_len]
        powers[i][1] = int(pow)

    powers.sort(key = lambda x : x[1], reverse=True)

    for pow in powers:
        answer += str(pow[0])

    for _ in range(len(answer)-1):
        if answer[0] == '0':
            answer.pop(0)
        else:
            break
    answer = ''.join(answer)
    return answer



print(solution([0,0,0,0]))
# 9 99 997 878 87
# 8788 8787
print(solution([3, 30, 34, 5, 9]))