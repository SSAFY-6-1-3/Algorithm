equations = input().split('-')
nums = []

for equation in equations:
    num = sum(map(int, equation.split('+')))
    nums.append(num)

ans = nums[0]
for i in range(1, len(nums)):
    ans -= nums[i]

print(ans)