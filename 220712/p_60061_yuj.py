
def solution(n, build_frame):
    answer = []

    def check():
        for x, y, a in answer:
            # 기둥일 때
            # 바닥일 때, 다른 기둥 위에, 보의 한 쪽 끝
            if a == 0:
                if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                    pass
                else:
                    return 0
            # 보일 때
            # 한 쪽 끝이 기둥 위일 때, 양 쪽 끝이 보일 때
            else:
                if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer:
                    pass
                elif [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
                    pass
                else:
                    return 0
        return 1

    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:
            answer.append([x, y, a])
            if not check():
                answer.remove([x, y, a])
        else:
            answer.remove([x, y, a])
            if not check():
                answer.append([x, y, a])

    return sorted(answer)

print(solution(	5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(	5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))