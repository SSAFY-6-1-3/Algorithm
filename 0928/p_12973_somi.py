'''
짝지어 제거하기

'''

def solution(s):
    i = 0
    stack = []

    while i < len(s):
        if stack:  # stack에 알파벳 있는 경우
            if stack[-1] == s[i]:  # stack 맨 마지막 알파벳과 현재 인덱스 알파벳 비교
                stack.pop()        # 만약 같으면 stack에서 pop

            else:  # 만약 다른 알파벳이라면,
                stack.append(s[i])

        else:  # stack이 비어있는 경우,
            stack.append(s[i])  # 현재 인덱스 알파벳을 stack에 넣기

        i += 1 # 다음 인덱스로 이동

    # 줄일 방법 없을까?
    # return not stack # boolean....

    if len(stack) == 0:
        return 1
    else:
        return 0


print(solution('baabaa'))
print(solution('cdcd'))