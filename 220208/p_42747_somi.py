def solution(citations):

    citations.sort(reverse=True)  # 내림차순
    ans = 0
    for i in range(citations[0], -1, -1):  #  h-index 후보
        cnt = 0  # 인용된 횟수가 i 보다 많은 논문 개수 count
        for c in citations:
            if c >= i:
                cnt += 1
            else:
                break

        if cnt >= i: # i 번 인용된 논문이 i 편 이상이면 h-index
            ans = i
            break

    return ans

print(solution([3, 0, 6, 1, 5]))