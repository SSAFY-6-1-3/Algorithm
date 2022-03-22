def solution(nums):
    new_nums = set(nums)
    return min(len(nums)//2, len(new_nums))

