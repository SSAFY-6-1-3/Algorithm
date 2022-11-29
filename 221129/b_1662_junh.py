
st = input()
stack = []
tmp = ''
length = 0

for c in st:
    if c.isdigit():
        length += 1
        tmp = c
    elif c == '(':
        stack.append((tmp, length - 1))
        length = 0
    else:
        multi, preL = stack.pop()
        length = (int(multi) * length) + preL

print(length)