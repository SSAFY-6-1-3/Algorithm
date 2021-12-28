def solution(n, lost, reserve):
    answer = -1
    lost.sort()
    students = [1] * (n+1)
    for student in reserve:
        if student in lost:
            students[student] = 3
        else:
            students[student] = 2

    for idx in lost:
        if students[idx] == 3:
            students[idx] = 1
            continue

        if idx > 1:
            if students[idx-1] == 2:
                students[idx-1] = 1
                students[idx] = 1
                continue
        if idx < n:
            if students[idx+1] == 2:
                students[idx+1] = 1
                students[idx] = 1
                continue
        students[idx] = 0

    for st in students:
        if st:
            answer += 1
    return answer

n = 3
lost = [3]
reserve = [1]
print(solution(n, lost, reserve))