
st = input()
stack = []
tmp = ''
idx = 0

while idx < len(st):
    if st[idx] == ')':
        popped = stack.pop()
        b = ''
        while popped != '(':
            b += popped
            popped = stack.pop()

        stack.append(b * a)
    elif st[idx] == '(':
        stack.append(st[idx])
    else:
        last = st[idx]
        stack.append(1)
    idx += 1

answer = 0
for c in stack:
    answer += len(c)
print(answer)