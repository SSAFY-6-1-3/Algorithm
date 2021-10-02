import sys
sys.stdin=open('input.txt')
input=sys.stdin.readline

while True:
    sentence = input()
    if sentence == '.':
        break

    braket = {')': '(', ']': '['}
    stack = []
    for word in sentence:
        if word in braket.values():             # 여는 괄호가 나오면 stack에 추가
            stack.append(word)

        elif word in braket:                    # 닫는 괄호일 경우
            if stack:                           # stack에 여는 괄호가 있을 경우 비교
                if stack[-1] == braket[word]:   # 짝이 맞다면 pop
                    stack.pop()
                else:                           # 짝이 다르다면 stack에 추가 -> no 나와야함
                    stack.append(word)
                    break                       # 이미 틀렸으니까 반복문 break
            else:
                stack.append(word)              # 닫는 괄호가 가장 먼저 나올 경우 -> no 나와야함
                break                           # 이미 틀렸으니까 반복문 break


    if not stack:
        print('yes')
    else:
        print('no')