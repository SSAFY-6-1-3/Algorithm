def solution(numbers, target):
    global cnt
    result = 0
    cnt = 0
    calculate(numbers, target, result, cnt)



def calculate(numbers, target, result, cnt):
    if not numbers:
        if result == target:
            cnt += 1
            return
        else:
            return

    calculate(numbers, target, result + numbers[0], cnt)
    calculate(numbers, target, result - numbers[0], cnt)


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))