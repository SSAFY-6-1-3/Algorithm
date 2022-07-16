def find_number(number):
    left = 0
    right = N - 1
    while left <= right:  # 이분탐색
        mid = (left + right) // 2
        if answers[mid] == number:
            return 1
        if answers[mid] > number:
            right = mid - 1
        else:
            left = mid + 1
    return 0


T = int(input())
for _ in range(T):
    N = int(input())  # 수첩 1에 적은 정수 수
    answers = list(map(int, input().split())) # 수첩1
    answers.sort()
    M = int(input())  # 수첩 2에 적은 정수 수
    questions = list(map(int, input().split()))
    for num in questions:
        print(find_number(num))
