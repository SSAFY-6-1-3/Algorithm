def solution(dep, budget): # 인자의 이름을 변경해도 작동합니다.
    answer = 0
    dep.sort() # 부서를 오름차순으로 정렬

    for d in dep: # 부서를 순회하며
        budget -= d # 예산에서 부서 금액을 뺀다.
        if budget < 0: # 예산이 마이너스가 되면
            return answer # 이전의 answer를 리턴
        answer += 1 # 아니면 answer +1

    return answer

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))