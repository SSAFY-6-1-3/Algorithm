'''
인형뽑기 게임

'''

def solution(board, moves):
    stack = []
    game_screen = list(map(list, zip(*board)))  # zip 사용하여 moves의 위치가 행이 될 수 있도록
    count = 0  # 인형 개수 세기

    for i in moves:
        doll = 0
        for j in range(len(game_screen)):
            if game_screen[i - 1][j]:         # 0이 아니라면
                doll = game_screen[i - 1][j]  # 해당 인형 번호를 변수에 저장하고
                game_screen[i - 1][j] = 0     # 해당 위치에 0을 저장
                break                         # 인형 찾으면 for문 빠져나오기

        if stack and stack[-1] == doll:       # stack의 마지막 인형과 동일한 인형이라면,
            stack.pop()                       # stack의 마지막 인형 빼기
            count += 2                        # 인형 수 +2
        elif doll:                            # stack에 인형 저장해야 하는 경우, (이때, doll 이 0이 아니여야함)
            stack.append(doll)

    return count

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
