def solution(s):
    s = s[2:-2].split('},{')
    # s[0] = s[0][2:]
    # s[-1] = s[-1][:-2]
    answer = []

    numSet = sorted(s, key=len)
    for numbers in numSet:
        numbers = list(map(int, numbers.split(',')))
        for num in numbers:
            if num not in answer:
                answer.append(num)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))