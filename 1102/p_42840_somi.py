def solution(answers):
    students = {
        1: [i for i in range(1, 6)],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    scores = [0, 0, 0, 0]

    for student in students:
        student_answer = students[student]
        s = len(student_answer)
        cnt = 0  # 맞춘 답 세기
        for a in range(len(answers)):
            if answers[a] == student_answer[a % s]:
                cnt += 1
        scores[student] = cnt

    max_ans = max(scores)
    answer = []
    for p in range(1, 4):
        if scores[p] == max_ans:
            answer.append(p)
    return answer

answers = [1,2,3,4,5]
print(solution(answers))