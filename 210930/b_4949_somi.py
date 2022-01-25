'''
균형잡힌 세상
'''
while True:
    sentence = input()

    if sentence == '.':     # 입력 종료 조건
        break               # 종료

    balance = 'yes'

    stack = []
    for w in sentence:
        if w == '(' or w == '[':  # 열린괄호 append
            stack.append(w)

        elif w == ')':
            if stack and stack[-1] == '(':  # 짝 맞는 지 확인
                stack.pop()
            else:
                balance = 'no'


        elif w == ']':
            if stack and stack[-1] == '[':
                stack.pop()

            else:
                balance = 'no'

    if stack:  # 남아있는 괄호 있으면 no
        balance = 'no'

    print(balance)
