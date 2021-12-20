import sys
input = sys.stdin.readline

N = int(input())
nums_dict = {}
nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)
    if num in nums_dict:
        nums_dict[num] += 1
    else:
        nums_dict[num] = 1

# 산술평균
print(round(sum(nums) / N))

# 중앙값
nums.sort()
print(nums[(N - 1)//2])

# 최빈값
cnt = max(nums_dict.values())
mode = []
for key, value in nums_dict.items():
    if value == cnt:
        mode.append(key)

mode.sort()
if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])

# 범위
print(max(nums) - min(nums))