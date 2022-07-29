from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
perms = permutations(nums, M)
for perm in sorted(list(perms)):
    print(*perm)