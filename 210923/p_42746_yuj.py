# 시간 초과
def solution(numbers):

    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i][0] < numbers[j][0]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
            elif numbers[i][0] == numbers[j][0]:
                if numbers[i]+numbers[j] < numbers[j]+numbers[i]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]


    result =  ''.join(numbers_str)
    return int(result)

numbers = [3, 30, 34, 5, 9]
# numbers = [0, 0, 0]
numbers_str = list(map(str,numbers))
print(solution(numbers_str))