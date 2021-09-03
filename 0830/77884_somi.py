def solution(left, right):
    answer = 0
    for number in range(left, right + 1): # left 부터 right 까지
        count = 0       # 약수의 개수
        for i in range(1, number + 1): # 1 ~ number 까지 약수인지 확인
            if number % i == 0:
                count += 1

        if count % 2: # 홀수라면
            answer -= number # 빼주기
        else: # 짝수라면
            answer += number # 더하기
