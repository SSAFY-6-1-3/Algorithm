def solution(board):
    h, w = len(board), len(board[0])


    for i in range(1, h):
        for j in range(1, w):
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i][j-1], board[i-1][j]) + 1

    max_len = max(map(max, board))
    return max_len ** 2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))