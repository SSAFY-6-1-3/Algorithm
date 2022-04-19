def solution(phone_number):
    star = len(phone_number) - 4
    answer = '*' * star
    answer += phone_number[-4:]

    return answer

print(solution("01033334444"))