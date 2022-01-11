# dp로 풀기!
# 대각선 아래 위치에 1이상의 값이 존재하면 현재 위치, 오른쪽, 왼쪽에서 정사각형 만들어지는지 확인
# 0 1                  2 2
# 1 1 이면 1 인 정사각형, 2 1 이런 경우에는 크기가 3인 정사각형
def solution(board):
    len_r = len(board)
    len_c = len(board[0])

    for r in range(len_r-1):
        for c in range(len_c-1):
            if board[r+1][c+1]:
                board[r+1][c+1] = min(board[r][c], board[r+1][c], board[r][c+1]) + 1
    return max(map(max, board)) ** 2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))


# 효율성 x
# def solution(board):
#     maxR = len(board)
#     maxC = len(board[0])
#     for l in range(min(maxR, maxC), 0, -1):
#         for i in range(maxR - l + 1):
#             for j in range(maxC - l + 1):
#                 answer = 0
#                 for y in range(j, j+l):
#                     for x in range(i, i+l):
#                         answer += board[x][y]
#                 if answer == l*l:
#                     return answer
#     else:
#         return 0