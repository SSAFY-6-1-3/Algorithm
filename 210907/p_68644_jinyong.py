def solution(numbers):
    temp = [0] * 201
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            n = numbers[i]+numbers[j]
            if not temp[n]:
                temp[n] = 1
    for i in range(201):
        if temp[i]:
            answer.append(i)
    return answer


print(solution([2, 1, 3, 4, 1]))