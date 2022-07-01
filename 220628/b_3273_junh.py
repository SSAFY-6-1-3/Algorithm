n = int(input())
li = list(map(int, input().split()))
x = int(input())

answer = 0
nums = set()
for i in range(n):
    jjak = x - li[i]
    if jjak in nums:
        answer += 1
    nums.add(li[i])

print(answer)