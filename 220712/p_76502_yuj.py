from collections import deque

def check(brackets):
    stack = []
    start = ['[', '{', '(']
    end = {']': '[', '}': '{', ')':'('}
    for bracket in brackets:
        if bracket in start:
            stack.append(bracket)
        elif bracket in end:
            if stack:
                br = stack.pop()
                if end[bracket] != br:
                    return 0
            else:
                return 0
        else:
            return 0
    if stack:
        return 0
    return 1

def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        temp = s.popleft()
        s.append(temp)
        if check(s):
            answer += 1
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("([{)}]"))