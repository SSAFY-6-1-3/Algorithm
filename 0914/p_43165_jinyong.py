operation = ['+', '-']
answer = 0


def ans_def(idx, numbers, num_sum, target):  # 깊이 우선 탐색 사용
    global answer

    if idx == len(numbers):  # 숫자를 전부 탐색했으면
        if num_sum == target:  # 지금까지의 연산이 타겟넘버와 같으면
            answer += 1  # 답을 1 증가
        return

    ans_def(idx+1, numbers, num_sum+numbers[idx], target)  # 현재 숫자를 더하고 다음 숫자로 넘어감
    ans_def(idx+1, numbers, num_sum-numbers[idx], target)  # 현재 숫자를 빼고 다음 숫자로 넘어감

    return answer


def solution(numbers, target):
    result = ans_def(0, numbers, 0, target)  # 위의 재귀 함수를 돌리고
    return result  # 결과 리턴


print(solution([1, 1, 1, 1, 1], 3))