jjak = {
    '[' : ']',
    '{' : '}',
    '(' : ')'
}

def check(st):
    stack = []
    for c in st:
        if c in '{[(':
            stack.append(c)
        else:
            if stack and jjak[stack[-1]] == c:
                stack.pop()
            else:
                return 0
    if stack: return 0
    return 1

def solution(s):
    answer = 0
    l = len(s)

    for _ in range(l):
        answer += check(s)
        s = s[1:] + s[0]

    return answer



print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
