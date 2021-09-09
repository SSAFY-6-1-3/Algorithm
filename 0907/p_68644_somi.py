'''
두개 뽑아서 더하기
'''


def solution(numbers):
    n = len(numbers)
    sum = []
    for i in range(0, n):
        for j in range(i+1, n):
            sum.append(numbers[i] + numbers[j]) # 두개씩 더하기
    answer = list(set(sum))  # set으로 바꿔서 중복 값 없애고 list로 변환
    answer.sort()  # 오름차순
    return answer


print(solution([2,1,3,4,1]))