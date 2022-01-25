def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append(" ")
    answer = ''
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer