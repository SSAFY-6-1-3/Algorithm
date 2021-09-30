import sys
sys.stdin = open('input.txt')
'''
흰색일 경우, 검정색이 쭉 나오다가 흰색이 나와야 중간에 색상들도 변경 가능 -> return 1
흰색으로 끝나지 않을 경우에는 중간에 색상들 변경할 수 없음 
'''
def find(i,j,k):
    global change_lst

    change_lst.append([i, j])                       # 현재 위치의 색상 변경되야하므로 추가

    if 0 < i + di[k] <= N and 0 < j + dj[k] <= N:   # 다음 위치가 보드판 범위 안에 있다면 이동
        i, j= i+di[k], j + dj[k]
        if board[i][j] == color:                    # 만약 다음 위치가 현재 색상이랑 똑같다면 1 return
            return 1
        elif board[i][j] == other:                  # 다음 위치가 아직도 다른 색상이라면 재귀
            if find(i, j, k):                       # 하면서 현재 색상과 같은 색상 나올 때까지 찾기
                return 1



T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())

    board = [[0] * (N+1) for _ in range(N+1)]         # 위치와 인덱스 숫자 맞추기 위해 위, 왼쪽 배열 한 줄 추가해서 보드 설정

    for k in range(N+1):                              # 배열 추가한 곳은 -1(맨 위, 맨 왼쪽)
        board[0][k] = -1
        board[k][0] = -1

    board[N//2][N//2+1], board[N//2+1][N//2] = 1, 1   # 가장 처음 말 위치 설정
    board[N//2][N//2], board[N//2+1][N//2+1] = 2, 2

        # 상 하 좌 우 대각선
    di = [-1, +1, 0, 0, +1, +1, -1, -1]
    dj = [0, 0, -1, +1, +1, -1, +1, -1]

    for _ in range(M):
        j, i, color = map(int,input().split())
        board[i][j] = color                         # 말 위치한 곳 해당 색상으로 바꾸기

        if color == 1:                              # 다른 색상 other로 설정
            other = 2
        else:
            other = 1


        for k in range(8):                          # 주위 둘러보면서 지금 색상이랑 다른 색상인 곳 찾기
            change_lst = []                         # 중간에 끼어서 색상 변경될 곳
            ni, nj = i + di[k], j + dj[k]

            if 0 < ni <= N and 0 < nj <= N:         # 보드판 안에 위치하고, 현재 위치 색상과 다른 색상이라면
                if board[ni][nj] == other:
                    if find(ni, nj, k):             # 가운데에 끼어있는지 확인
                        for a, b in change_lst:
                            board[a][b] = color


    black, white = 0, 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print('#{}'.format(tc), black, white)