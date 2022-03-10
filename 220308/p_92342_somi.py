# 중복조합 다른 사람 풀이 참고함
from itertools import combinations_with_replacement

def solution(n, info):
    ans = [-1] * 12
    for comb in combinations_with_replacement(range(11), n):  #n개 화살 과녁 맞힌 조합
        arrow = [0] * 12  # 맨 마지막은 점수차이 [10, 9, ~ 0, 점수차이]
        score = 0  # 점수 차이
        for x in comb:
            arrow[x] += 1

        for i in range(11):
            if arrow[i] > info[i]:  # 라이언
                score += (10 - i)
            elif info[i] != 0:      # 어피치
                score -= (10 - i)
        if score <= 0:
            continue
        arrow[11] = score

        if arrow[::-1] > ans[::-1]:  # 방법이 여러가지인 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 리턴
            ans = arrow

    if ans[-1] == -1:  # 라이언이 우승할 방법이 없는 경우
        return [-1]

    return ans[:-1]
