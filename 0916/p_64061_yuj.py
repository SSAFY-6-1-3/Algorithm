def solution(board, moves):
    N = len(board[0])                   # NxN 크기의 뽑기판이니까 N 구하기
    stack = []                          # 인형 집어넣을 바구니
    cnt = 0                             # 사라진 인형의 개수

    for j in moves:                     # moves 리스트에서 해당 열의 가장 위의 인형 뽑기
        for i in range(N):
            if board[i][j-1]:
                if stack and (stack[-1] == board[i][j-1]):      # 넣을 인형이 stack의 마지막 인형이랑 비교
                    stack.pop()                                 # 마지막 인형과 같은 인형이라면 마지막 인형 빼기
                    cnt += 2                                    # 총 2개의 인형이 빠짐
                    break
                else:
                    stack.append(board[i][j-1])                 # 마지막 인형이랑 같은 인형이 아니라면 바구니에 인형 추가
                    break
        board[i][j - 1] = 0                                     # 크레인으로 뽑은 인형 0으로 바꿔주기

    return cnt



board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))