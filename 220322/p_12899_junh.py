def solution(n):
    answer = ''
    stack = []
    dic124 = {1:'1', 2:'2', 0:'4'}
    while n>0:
        stack.append(dic124[n%3])
        n = (n-1)//3**len(stack)
    while stack:
        answer += str(stack.pop())

    return answer


print(solution(1))
print(solution(5))
print(solution(6))
print(solution(9))
print(solution(10))