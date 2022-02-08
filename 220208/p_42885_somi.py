# 2명만 타는 것 고려 안함
# def solution(people, limit):
#     answer = 0
#     people.sort(reverse=True)
#     saved = [False] * len(people)
#
#     for i in range(len(people)):
#         if not saved[i]:
#             answer += 1
#             weight = people[i]
#             for j in range(len(people)-1, i, -1):
#                 if not saved[j] and weight + people[j] <= limit:
#                     weight += people[j]
#                     saved[j] = True
#     return answer

def solution(people, limit):
    answer = 0  # 배 개수
    people.sort()  # 오름차순으로 정렬
    saved = [False] * len(people)  # 구조 여부
    idx = 0  # 가벼운 사람 인덱스 번호
    for i in range(len(people) - 1, -1, -1):  # 무거운 사람 먼저 태우고
        if not saved[i]:
            answer += 1
            if people[i] + people[idx] <= limit:  # 가벼운 사람 한명 태우기
                saved[idx] = True
                idx += 1

    return answer

print(solution([70, 50, 80, 50], 100))