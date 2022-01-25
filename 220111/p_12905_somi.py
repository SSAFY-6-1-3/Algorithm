# 하........dp............

def solution(board):
    n = len(board)
    m = len(board[0])
    cnt = [board[0]] + [[0 for _ in range(m)] for _ in range(n - 1)]
    for r in range(1, n):
        cnt[r][0] = board[r][0]

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j]:
                cnt[i][j] = min(cnt[i - 1][j - 1], cnt[i - 1][j], cnt[i][j-1]) + 1

    answer = max(map(max, cnt)) ** 2



    return answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))