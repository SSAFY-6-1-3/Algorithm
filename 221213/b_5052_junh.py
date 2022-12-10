t = int(input())
for _ in range(t):
    n = int(input())
    nums = [input() for _ in range(n)]
    nums.sort()

    for i in range(n-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            print('NO')
            break
    else:
        print('YES')
