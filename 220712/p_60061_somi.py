def check(ans):
    for build in ans:
        x, y, a = build
        if a == 0:  # 기둥
            # 바닥, 보 위, 다른 기둥 위
            if y == 0 or\
                    [x - 1, y, 1] in ans or \
                    [x, y, 1] in ans or \
                    [x, y - 1, 0] in ans:
                continue
            return False

        elif a == 1:  # 보
            # 기둥 위, 다른보 연결
            if [x, y - 1, 0] in ans or\
                [x + 1, y - 1, 0] in ans or \
                    ([x - 1, y, 1] in ans and [x + 1, y, 1] in ans):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, a, b = build
        if b == 0:
            answer.remove([x, y, a])  # 일단 빼고 체크
            if not check(answer):
                answer.append([x, y, a])

        else:
            answer.append([x, y, a])  #
            if not check(answer):
                answer.remove([x, y, a])


    answer.sort()
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))

