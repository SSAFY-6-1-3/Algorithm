def permu(now_num, result, depth):
    if depth == M:
        permus.append(result)
        return

    for i in range(now_num, N):
        num = nums[i]
        permu(i, result+[num], depth+1)

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
permus = []
permu(0, [], 0)
for perm in permus:
    print(*perm)