def solution(numbers):
    answer = []
    length = len(numbers)
    powers = [[numbers[i], 0] for i in range(length)] # [숫자, 숫자 반복한 문자열]

    for i in range(length):
        num = str(numbers[i]) # numbers의 각 숫자
        n_len = len(num)
        pow = '' # 앞에 붙어있을때 수의 가치
        for k in range(4): # 1000(10의 네제곱) 
            pow += num[k%n_len] # num을 반복하여 쌓기
        powers[i][1] = int(pow) # num의 반복을 int로 변환하여 저장

    powers.sort(key = lambda x : x[1], reverse=True) # 반복하여 int로 변환환 수의 크기로 내림차순 정렬

    for pow in powers:
        answer += str(pow[0]) # 순서대로 문자열의 형태로 쌓고

    for _ in range(len(answer)-1): # 앞에 의미없는 '0'제거
        if answer[0] == '0':
            answer.pop(0)
        else:
            break
    answer = ''.join(answer) # dd
    return answer



print(solution([0,0,0,0]))
# 9 99 997 878 87
# 8788 8787
print(solution([3, 30, 34, 5, 9]))