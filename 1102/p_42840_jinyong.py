def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    num = [a, b, c]
    best = []
    answer = []

    for man in num:
        count = 0
        x, y = divmod(len(answers), len(man))
        test = man*x

        for i in range(y):
            test.append(man[i])

        for j in range(len(answers)):
            if answers[j] == test[j]:
                count += 1

        best.append(count)

    for k in range(1, 4):
        if best[k-1] == max(best):
            answer.append(k)

    return answer


# print(solution([1,2,3,4,5]))


def solution2(answers):

    length = len(answers)
    # 수포자 1
    total1 = 0
    num = 0
    for i in range(length):
        num = num % 5 + 1
        if answers[i] == num:
            total1 += 1

    # 수포자 2
    total2 = 0
    num = 0
    for i in range(length):
        if num == 2:
            num += 1

        if not i % 2:
            if answers[i] == 2:
                total2 += 1
        else:
            num = num % 5 + 1
            if answers[i] == num:
                total2 += 1

    # 수포자 3
    total3 = 0
    num, check = 0, 0
    lst = [3, 1, 2, 4, 5]
    for i in range(length):
        if answers[i] == lst[num]:
            total3 += 1
        check += 1
        if check == 2:
            check = 0
            num = (num + 1) % 5

    answer = []

    values = [total1, total2, total3]
    maximum = max(values)
    for i in range(3):
        if values[i] == maximum:
            answer.append(i+1)

    return answer


print(solution2([1, 2, 3, 4, 5]))
print(solution2([1, 3, 2, 4, 2]))
print(solution2([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]))
