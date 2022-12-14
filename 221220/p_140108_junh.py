
def solution(s):
    answer = 0
    a, b = 0, 0
    idx = 0

    while idx < len(s):
        if a == b == 0:
            std = idx
        if s[idx] == s[std]:
            a += 1
        else:
            b += 1
        if a == b:
            answer += 1
            a, b = 0, 0
        idx += 1

    if a + b:
        answer += 1
    return answer


print(solution("aaabbaccccabba"))