def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        answer += num                       # 일단 숫자 다 더해줌
        for i in range(1, num+1):
            if num == (i**2):               # 완전 제곱수인 경우에만 약수 개수가 홀수
                answer -= (num*2)           #  더해줬던 숫자까지 빼주기
                break

    return answer

left, right = map(int, input().split())
print(solution(left, right))
