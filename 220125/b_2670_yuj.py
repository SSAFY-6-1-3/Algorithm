N = int(input())
nums = [float(input()) for _ in range(N)]

for i in range(N-1):
    nums[i+1] = max(nums[i+1], nums[i+1] * nums[i])

print("%.3f"%max(nums))                     # round 쓰니까 틀림,,