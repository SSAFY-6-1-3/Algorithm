
def is_bingo():
    cnt = 0

    # 가로
    for i in range(5):
        if sum(bingo[i]) == 0:
            cnt += 1

    # 세로
    c = 0
    while c < 5:
        col = 0
        for j in range(5):
            col += bingo[j][c]

        if col == 0:
            cnt += 1
        c += 1

    # 대각선
    dig = 0
    rdig = 0
    for a in range(5):
        dig += bingo[a][a]
        rdig += bingo[a][4 - a]

    if dig == 0:
        cnt += 1
    if rdig == 0:
        cnt += 1

    return cnt

def check(ans):
    for r in range(5):
        for c in range(5):
            if bingo[r][c] == ans:
                bingo[r][c] = 0
                return


bingo = [list(map(int, input().split())) for _ in range(5)]  # 철수 빙고판
answer = []  # 사회자
for _ in range(5):
    answer += list(map(int, input().split()))

for i in range(25):
    check(answer[i])
    bingo_cnt = is_bingo()
    if bingo_cnt >= 3:
        print(i + 1)
        exit()
