def solution(s):
    answer = -1
    stack = [0]
    for c in s:
        if c == stack[-1]:
            stack.pop(-1)
        else:
            stack.append(c)

    if len(stack)>1:
        return 0
    else:
        return 1


print(solution('baabaa'))