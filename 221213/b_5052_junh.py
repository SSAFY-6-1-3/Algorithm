t = int(input())
for _ in range(t):
    n = int(input())
    nums = [input() for _ in range(n)]
    nums.sort(key= lambda x: -len(x))
    print(nums)
    dic = {}