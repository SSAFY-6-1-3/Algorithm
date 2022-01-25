def solution(participant, completion):
    p = sorted(participant) # 이름 순으로 sort
    c = sorted(completion)

    answer = 0
    for i in range(len(c)):
        if p[i] != c[i]: # 순서대로 대조해서 다르면 답
            answer = p[i]
            return answer
    answer = p[-1]  # 만약 completion 다 돌았는데 아직 남아있으면 participant의 맨 마지막 사람이 답!
    return answer


# 나와 비슷한 다른사람의 풀이
# 1) answer를 고수할필요가 없었음!!!!!
# 2) sort 활용!
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

