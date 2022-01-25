def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    stack = ''
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        elif s[i].isalpha():
            stack += s[i]  # 글자는 stack에 모아두었다가
            if stack in numbers:  # 단어가 완성되면
                answer += str(numbers.index(stack))  # 인덱스값을 answer에 작성
                stack = ''  # 한 단어 완성된 후에는 stack 을 초기화
    return int(answer)


# 다른사람 풀이
# 딕셔너리, replace 활용!!

def solution2(s):
    numbers_dictionary = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    answer = s
    for key, value in numbers_dictionary.items():
        answer = answer.replace(key, value)
    return int(answer)

print(solution2("2three45sixseven"))