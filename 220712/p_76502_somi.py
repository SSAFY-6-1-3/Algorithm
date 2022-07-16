def check(arr):
    _open = {'{': 0, '[' : 1, '(' : 2}
    _close = ['}', ']', ')']
    stack = []
    flag = True
    for char in arr:
        if char in _open:
            stack.append(char)
        elif char in _close and stack:
            left = stack.pop()
            if _close[_open[left]] != char:
                flag = False
                break
        else:  # 괄호가 아니거나, 여는괄호 나오기전에 닫는괄호 먼저 나온 경우
            flag = False
            break
    if stack:  # 여는괄호 남아있으면
        flag = False
    return flag

def solution(s):
    answer = 0
    x = len(s)
    s += s
    for i in range(x):
        if check(s[i: x + i]):
            answer += 1
    return answer



print(solution('()('))
