def divide(s, e, N):
    global answer
    flag = 1
    for i in range(s, s+N):
        for j in range(e, e+N):
            if papers[i][j] != papers[s][e]:
                flag = 0
                break
        if not flag:
            break

    else:
        if papers[s][e] == -1:
            answers[0] += 1
        elif papers[s][e] == 0:
            answers[1] += 1
        else:
            answers[2] += 1
        return

    for r in range(3):
        for c in range(3):
            divide(s+r*(N//3), e+c*(N//3), N//3)

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
answers = [0, 0, 0]
divide(0, 0, N)
for answer in answers:
    print(answer)