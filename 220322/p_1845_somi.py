def solution(nums):
    cnt = len(nums) // 2
    poketmons = list(set(nums))
    ans = cnt  # 전부 다른 종류 뽑는 경우

    if len(poketmons) < cnt:  # 종류가 부족해서 중복해서 뽑아야하는 경우
        ans = len(poketmons)

    return ans




print(solution([3,3,3,2,2,4]))