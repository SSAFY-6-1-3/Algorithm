def solution(operations):       # 왜 됨?????
    q = []

    for oper in operations:
        if oper[0] == 'I':
            num = int(oper[2:])
            q.append(num)
            q.sort()
        elif q:
            if oper[2] == '1':
                q.pop()
            else:
                q.pop(0)
    if q:
        answer = [max(q), min(q)]
        return answer
    else:
        return [0, 0]


print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))