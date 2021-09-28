def solution(s):

    queue = []
    for alpha in s:                     # s 문자열에서 하나씩 queue리스트에 추가
        if queue:                       # queue안에 숫자가 있다면
            if queue[-1] == alpha:      # queue의 마지막 숫자와 지금 들어갈 숫자와 비교
                queue.pop()             # 둘이 같다면 pop
            else:
                queue.append(alpha)     # 다르다면 queue에 추가해주기
        else:                           # queue가 비어있다면 단어 바로 추가해주기
            queue += alpha

    if queue:                           # 결과적으로 queue가 비어있다면 1, 남아있는 단어가 있다면 0 출력
        answer = 0
    else:
        answer = 1
    return answer

s = 'cdcd'
print(solution(s))