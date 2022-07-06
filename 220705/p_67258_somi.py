# 2중 for문은 효율성검사에서 통과 안됨.

def solution(gems):
    answer = [1, len(gems)]
    gem_cnt = len(set(gems))  # 보석 종류 개수
    if gem_cnt == len(gems):
        return answer
    else:
        start = 0
        end = 0
        buy = {gems[0]: 1}
        while start <= end:
            if len(buy) == gem_cnt:
                if answer[1] - answer[0] > end - start:  # 싹쓰리 구간이 짧다면
                    answer = [start + 1, end + 1]
                buy[gems[start]] -= 1
                if buy[gems[start]] == 0:
                    del buy[gems[start]]
                start += 1

            else:
                end += 1
                if end == len(gems):
                    break
                if gems[end] in buy:
                    buy[gems[end]] += 1
                else:
                    buy[gems[end]] = 1
    return answer


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
