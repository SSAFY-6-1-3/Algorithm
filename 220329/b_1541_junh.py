

st = input()
nums = []
tmp = ''

idx = 0
while idx < len(st):
    if st[idx] in "+-":
        nums.append(int(tmp))
        tmp = ''
    tmp += st[idx]
    idx += 1
nums.append(int(tmp))

minus = False
answer = 0
for num in nums:
    if num<0:
        minus = True

    if minus:
        answer -= abs(num)
    else:
        answer += num

print(answer)