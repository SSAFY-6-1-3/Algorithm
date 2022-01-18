
import sys
sys.stdin = open('s_3752_input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))

    grade = [0]  # 가능한 모든 점수 저장, 0점은 무조건

    for score in scores:  # 각 문제에 대해서
        for i in range(len(grade)):
            tmp = score + grade[i]
            grade.append(tmp)
        grade = list(set(grade))


    print(f'#{tc} {len(grade)}')
