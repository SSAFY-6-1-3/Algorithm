def solution(nums):
    n = len(nums)
    n_set = set(nums)
    if len(n_set) < n//2:
        return len(n_set)
    return n//2



print(solution([3,1,2,3]))