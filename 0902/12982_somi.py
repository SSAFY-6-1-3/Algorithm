'''
예산
'''

def solution(d, budget):
    d.sort()  # 부서별 예산 신청 금액을 정렬
    sub_sum = 0  # 부서에서 신청한 금액 더해 줄 변수
    answer = 0   # 지원 가능한 부서 수
    for i in range(len(d)):  # 작은 신청액부터 더해나가기
        sub_sum += d[i]
        if sub_sum > budget:  # 만약 예산액을 넘는다면 break로 끝내기
            break
        answer += 1  # 지원 가능하다면 부서 수 증가
    return answer


# 첫번째 틀린 풀이
# 부분집합을 구하고, 그 부분집합의 합을 구함
# 시간 초과에 심지어 답도 틀린것이 있었음
# 복잡하게 생각말자
# def solution(d, budget):
#     n = len(d)
#     subset = []
#     for i in range(1 << n):
#         sub = []
#         for j in range(n):
#             if i & (1 << j):
#                 sub.append(d[j])
#         subset.append(sub)
#
#
#     answer = 0
#     for k in range(len(subset)-1, -1, -1):
#         if sum(subset[k]) == budget and answer < len(subset[k]):
#             answer = len(subset[k])
#     return answer

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))