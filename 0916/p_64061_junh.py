def solution(board, moves):
    stack = []
    answer = 0
    size = len(board)
    board2 = [[0] * size for _ in range(size)]
    for r in range(size):
        for c in range(size):
            board2[c][r] = board[r][c]

    for move in moves:
        move -= 1
        kakao = 0

        for i in range(size):
            if board2[move][i]:
                kakao = board2[move][i]
                board2[move][i] = 0

                if stack and stack[-1] == kakao:
                    stack.pop(-1)
                    answer += 2
                else:
                    stack.append(kakao)
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))