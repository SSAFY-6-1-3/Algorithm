'''
타겟넘버

빼야 할 숫자의 합 = (총합 - 타겟넘버) * (1/2)
빼야 할 숫자의 합을 만들기

A + B = 총합
A - B = 타겟넘버
'''

def solution(numbers, target):
    n = len(numbers)  # n개의 정수
    total = sum(numbers)  # 숫자들의 총합
    subtract = int((total - target) * 0.5)  # 빼야할 숫자들의 합
    count = 0  # 타겟 넘버 만든는 방법의 수 세기

    for i in range(1 << n):  # 빼야 할 숫자들이 될 부분집합 구하기
        sub_sum = 0  # 부분집합의 합 구하기
        for j in range(n):
            if i & (1 << j):
                sub_sum += numbers[j]
                if sub_sum > subtract:  # 부분집합의 합이 빼야 할 숫자의 합보다 커지면 break
                    break
        if sub_sum == subtract:  # 해당 부분집합이 빼야 할 숫자들의 합과 동일하다면
            count += 1  # 방법 1 추가

    return count

print(solution([1, 1, 1, 1, 1], 3))







