res = 0
minus = input().split('-')
for i in range(len(minus)):
    nums = minus[i]
    temp = 0
    plus = nums.split('+')
    for num in plus:
        temp += int(num)
    if i == 0:
        res += temp
    else:
        res -= temp
print(res)
