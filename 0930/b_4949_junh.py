while True:
    st = input()
    if st ==".":
        break

    stack = []
    for c in st:
        if c == '(' or c=='[':
            stack.append(c)
        elif not stack and (c == ')' or c == ']'):
            print('no')
            break
        elif c ==')' and stack.pop() != '(':
            print('no')
            break
        elif c == ']' and stack.pop() != '[':
            print('no')
            break
    else:
        if stack:
            print('no')
        else:
            print('yes')
