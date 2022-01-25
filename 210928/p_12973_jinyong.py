def solution(s):
    temp = []
    for i in range(len(s)):
        if not temp:
            temp.append(s[i])
        else:
            if temp[-1] != s[i] :
                temp.append(s[i])
            else:
                temp.pop()
    if not temp:
        return 1
    else:
        return 0


print(solution('baba'))
