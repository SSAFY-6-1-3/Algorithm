def solution(n, lost, reserve):
    # 도둑맞은 학생 중, 여분이 있었던 학생은 미리 빼주기
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))

    # 체육복 빌리기 전, 수업을 들을 수 있는 학생 수
    max_student = n - len(lost)

    for i in range(len(lost)):
        if lost[i] - 1 in reserve:
            max_student += 1
            reserve.remove(lost[i] - 1)

        elif lost[i] + 1 in reserve:
            max_student += 1
            reserve.remove(lost[i] + 1)

    return max_student
