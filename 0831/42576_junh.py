def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if i==len(completion) or participant[i] != completion[i]:
            return participant[i]