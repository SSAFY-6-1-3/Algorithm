# 효율성 0,,
def solution(participant, completion):
    answer = ''
    for part in participant:
        if part in completion:
            completion.remove(part)
        else:
            answer += part
    return answer
