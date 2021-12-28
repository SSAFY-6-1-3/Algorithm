T = int(input())
for _ in range(T):
    words = input()
    stack = []
    temp = []
    for word in words:
        if word == '<':
            if stack:
                temp.append(stack.pop())
        elif word == '>':
            if temp:
                stack.append(temp.pop())
        elif word == '-':
            if stack:
                stack.pop()
        else:
            stack.append(word)
    temp.reverse()
    print(''.join(stack+temp))

# 이런식으로 출력하면 런타임에러
#     if temp:
#         stack += temp.reverse()
#     print(*stack)