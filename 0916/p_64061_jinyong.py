def solution(board, moves):
    answer = 0
    doll_stack = [0]
    for move in moves:  # 인형을 뽑을 위치에 순서대로 접근
        for board_ele in board:
            catch = board_ele[move-1]  # 현재 줄의 i-1 번 인덱스 자리의 인형을 선택
            if catch:
                board_ele[move-1] = 0  # 인형이 현재 자리에서 없어졌다고 표시
                if catch == doll_stack[-1]:  # 만약 바구니의 맨 위에 같은 인형이 있으면
                    doll_stack.pop()  # 폭파
                    answer += 2
                else:
                    doll_stack.append(catch)  # 아니면 바구니의 맨 위에다가 올린다
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
