def solution(nums):
    nums_set = set(nums)

    if len(nums_set) >= len(nums)/2:
        answer = int(len(nums)/2)
    else:
        answer = len(nums_set)

    return answer
