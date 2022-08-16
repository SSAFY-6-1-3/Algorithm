N = int(input())
nums = list(map(int, input().split()))
new = sorted(list(set(nums)))
dic = dict()
ans = []
for idx in range(len(new)):
    dic[new[idx]] = idx
for num in nums:
    ans.append(dic[num])

print(*ans)