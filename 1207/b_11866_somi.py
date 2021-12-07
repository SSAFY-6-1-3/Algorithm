N, K = map(int, input().split())
nums = [i for i in range(1, N + 1)]
now = 0
print('<', end='')
# ans = []

while len(nums):
    now = (now + K - 1) % len(nums)
    # ans.append(nums.pop(now))
    if len(nums) == 1:
        print(nums.pop(now), '>', sep='',)  # 마지막 숫자 다음엔 닫힌 괄호
    else:
        print(nums.pop(now), ',', sep='', end=' ')


