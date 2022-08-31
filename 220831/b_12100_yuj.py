import copy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
def game(brd, k):
    tmp = [[0] * N for _ in range(N)]                   # 숫자들 한 방향으로 붙이기
    result = [[0] * N for _ in range(N)]                # 같은 숫자 더하기
    # 위
    if k == 0:
        for j in range(N):                              # 0아닐 경우에만 tmp에 저장해주기
            c = 0
            for i in range(N):
                if brd[i][j]:
                    tmp[c][j] = brd[i][j]
                    c += 1
            q, m = 0, 0
            while q < c-1:                              # 현재 숫자랑 그 다음 숫자 비교
                if tmp[q][j] == tmp[q+1][j]:            # 같으면 더하기
                    result[m][j] = 2*tmp[q][j]
                    q += 2
                else:                                   # 다르면 현재 숫자 그대로 표시
                    result[m][j] = tmp[q][j]
                    q += 1
                m += 1
            if q == c-1:                                # 마지막 숫자 비교 못 한 경우
                result[m][j] = tmp[q][j]
    # 아래
    if k == 1:
        for j in range(N):
            c = N-1
            for i in range(N-1, -1, -1):
                if brd[i][j]:
                    tmp[c][j] = brd[i][j]
                    c -= 1
            q, m = N-1, N-1
            while q > c+1:
                if tmp[q][j] == tmp[q - 1][j]:
                    result[m][j] = 2 * tmp[q][j]
                    q -= 2
                else:
                    result[m][j] = tmp[q][j]
                    q -= 1
                m -= 1
            if q == c + 1:
                result[m][j] = tmp[q][j]
    # 왼쪽
    if k == 2:
        for i in range(N):
            c = 0
            for j in range(N):
                if brd[i][j]:
                    tmp[i][c] = brd[i][j]
                    c += 1
            q, m = 0, 0
            while q < c-1:
                if tmp[i][q] == tmp[i][q+1]:
                    result[i][m] = 2*tmp[i][q]
                    q += 2
                else:
                    result[i][m] = tmp[i][q]
                    q += 1
                m += 1
            if q == c-1:
                result[i][m] = tmp[i][q]
    # 오른쪽
    if k == 3:
        for i in range(N):
            c = N-1
            for j in range(N-1, -1, -1):
                if brd[i][j]:
                    tmp[i][c] = brd[i][j]
                    c -= 1
            q, m = N-1, N-1
            while q > c+1:
                if tmp[i][q] == tmp[i][q-1]:
                    result[i][m] = 2*tmp[i][q]
                    q -= 2
                else:
                    result[i][m] = tmp[i][q]
                    q -= 1
                m -= 1
            if q == c+1:
                result[i][m] = tmp[i][q]

    return result

def move(brd, cnt):
    global ans

    if cnt == 5:
        temp = max(list(map(max, brd)))
        ans = max(ans, temp)
        return

    for k in range(4):
        tmp_board = copy.deepcopy(game(brd, k))
        move(tmp_board, cnt+1)

move(board, 0)
print(ans)