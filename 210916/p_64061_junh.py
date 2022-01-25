def solution(board, moves):
    stack = [] # 인형을 저장할 스택
    answer = 0
    size = len(board)
    board2 = [[0] * size for _ in range(size)] # board를 옆으로 돌려서 복사할 배열
    for r in range(size):
        for c in range(size):
            board2[c][r] = board[r][c] # 열과 행을 바꿔서 돌림

    for move in moves:
        move -= 1 # idx로 사용하기 위해 -1
        kakao = 0 # 뽑은 인형을 저장할 변수

        for i in range(size):
            if board2[move][i]: # move번째 배열에 뽑을게 있으면
                kakao = board2[move][i] # kakao에 저장
                board2[move][i] = 0 # 배열의 숫자를 0으로 만든다

                if stack and stack[-1] == kakao: # 스택 인형과 kakao가 같으면
                    stack.pop(-1) # 그 인형을 없앤다.
                    answer += 2 # 총 2개가 없어진거니 +2
                else:
                    stack.append(kakao) # 다르면 스택에 추가
                break # 인형을 뽑았을 경우 break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))